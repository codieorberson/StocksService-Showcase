
from flask import jsonify
from flask_classful import FlaskView
from flask_restful import Resource, reqparse
from flask_classful import FlaskView, route
from Helpers.JsonHelper import JsonHelper
from Models.GoogleSearchResults import FullGoogleSearchResults, GoogleSearchResults
from Services.AIService import AIService
import json
import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
import pickle
from keras.models import load_model
from keras.layers import Dropout
from keras.regularizers import l2
from keras.optimizers import RMSprop

class AIController(FlaskView):

    def __init__(self):
        self.aiService = AIService()
        self.jsonHelper = JsonHelper()
        
    @route('/BuildRNN', methods=['POST'])
    def BuildRNN(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("Gain")
        params = parser.parse_args()
        stockName= params["Name"]
        gain= params["Gain"]
        with open(f'Reports/News/{stockName}-FullNewsReports.json') as f:
            data = json.load(f)
        news = [FullGoogleSearchResults(**item) for item in data]
        for new in news:
            new.Title = new.Title.lower()
            sentimentLabel= self.jsonHelper.GetSentimentIntLabel(getattr(new, gain))
            setattr(new, gain, sentimentLabel)

        df = pd.DataFrame([vars(f) for f in news])
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(df['Title'])
        sequences = tokenizer.texts_to_sequences(df['Title'])
        X = pad_sequences(sequences, maxlen=100)
        y = df[gain].values

        model = Sequential()
        model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64))
        model.add(LSTM(64, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(32))
        model.add(Dense(1, activation='linear', kernel_regularizer=l2(0.01)))
        model.compile(optimizer=RMSprop(learning_rate=0.001), loss='mean_squared_error')
        #model.compile(optimizer='adam', loss='mean_squared_error')
        validationSplit = 0.2

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train, validation_split=validationSplit, epochs=100, batch_size=16)
        model.save(f'AIModels/RNN/{stockName}-{gain}-model.h5') 
        with open(f'AIModels/RNN/{stockName}-{gain}-tokenizer.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        return 'True'


    @route('/RNNPredictOffTitle', methods=['POST'])
    def RNNPredictOffTitle(self):
        vectorizer = CountVectorizer()
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("Gain")
        parser.add_argument("Search")
        params = parser.parse_args()
        stockName= params["Name"]
        gain= params["Gain"]
        search= params["Search"]
        modelName = f'AIModels/RNN/{stockName}-{gain}-model.h5'
        tokenizerName = f'AIModels/RNN/{stockName}-{gain}-tokenizer.pickle'

        predictions = self.RNNPredictGain(search, modelName, tokenizerName)
        return str(predictions)
    
    def RNNPredictGain(self, title, modelName, tokenizerName):
        try:
            with open(tokenizerName, 'rb') as file:
                tokenizer = pickle.load(file)
            model = load_model(modelName)
            text = [title]
            sequences = tokenizer.texts_to_sequences(text)
            X = pad_sequences(sequences)
            predictions = model.predict(X)
            return predictions
        except Exception as e:
            print(str(e))
            
        
    @route('/BuildNLP', methods=['POST'])
    def BuildNLP(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("Gain")
        params = parser.parse_args()
        stockName= params["Name"]
        gain= params["Gain"]
        with open(f'Reports/News/{stockName}-FullNewsReports.json') as f:
            data = json.load(f)
        news = [FullGoogleSearchResults(**item) for item in data]
        for new in news:
            sentimentLabel= self.jsonHelper.GetSentimentIntLabel(getattr(new, gain))
            setattr(new, gain, sentimentLabel)

        
        df = pd.DataFrame([vars(f) for f in news])
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(df['Title'])
        y = df[gain]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        joblib.dump(regressor, f'AIModels/NLP/{stockName}-{gain}-model.pkl')
        joblib.dump(vectorizer, f'AIModels/NLP/{stockName}-{gain}-vectorizer.pkl')

        
        return 'True'
    
    @route('/NLPPredictOffTitle', methods=['POST'])
    def NLPPredictOffTitle(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        parser.add_argument("Gain")
        parser.add_argument("Search")
        params = parser.parse_args()
        stockName= params["Name"]
        gain= params["Gain"]
        search= params["Search"]
        modelName = f'AIModels/NLP/{stockName}-{gain}-model.pkl'
        vectorName = f'AIModels/NLP/{stockName}-{gain}-vectorizer.pkl'
        predictions = self.NLPPredictGain(search, modelName, vectorName)
        return str(predictions)

    def NLPPredictGain(self, title, modelName, vectorName ):
        vectorizer = joblib.load(vectorName)
        model = joblib.load(modelName)
        titleVectorized = vectorizer.transform([title])
        predictions = model.predict(titleVectorized)
        return predictions
        
    @route('/BuildTestingModel', methods=['POST'])
    def BuildTestingModel(self):
        startTime = datetime.datetime.now()
        print("AIController.BuildRNNModel")
        parser = reqparse.RequestParser()
        parser.add_argument("Name")
        params = parser.parse_args()
        name= params["Name"]
        reports = self.aiService.BuildTestingModel(name)

        reports.sort(key=lambda item : item.Date)
        serializedNews = []
        for item in reports:
            serializedItem = {
                "Name": item.Name,
                "Date": item.Date,
                "Title": item.Title,
                "Worth": item.Worth,
                "Url": item.Url,
                "OneDayGain": item.OneDayGain,
                "ThreeDayGain": item.ThreeDayGain,
                "OneWeekGain": item.OneWeekGain[0],
                "TwoWeekGain" : item.TwoWeekGain[0],
                "OneMonthGain" : item.OneMonthGain,
                "Description" : item.Description,
            }
            serializedNews.append(serializedItem)
        jsonData = json.dumps(serializedNews)
        filePath = f'Reports/News/{name}-FullNewsReports.json'
        with open(filePath, 'w') as file:
            file.write(jsonData)
        print(f'Took this long to run: {datetime.datetime.now() - startTime}')
        return jsonData
    

    
    
    
    
    
   