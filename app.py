from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


app = Flask(__name__)
model = pickle.load(open("sgd_mod.sav", "rb"))

model_p = pickle.load(open("rf_random_1.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        day = datetime.strptime(date_dep, "%Y-%m-%dT%H:%M").weekday()
        # print(day)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        #Weekday
        #Dep_Weekday = request.form["Out_Weekday"]

        # Category
        Category = int(request.form["Sort"])

        #Price
        Price = int(request.form["rawtext"])
    

        # Duration
        Travel_Time = int(request.form["rawtext1"])

        # Total Stops
        Total_stops = int(request.form["Stops"])
        # print(Total_stops)

        # Airline
        airline=request.form['airline']
        if(airline=='IndiGo'):
            IndiGo = 1
            GoAir = 0
            Air_India = 0 
            SpiceJet = 0
            AirAsia_India = 0
            Vistara = 0
            Multiple_Airlines = 0

        elif(airline=='GoAir'):
            IndiGo = 0
            GoAir = 1
            Air_India = 0 
            SpiceJet = 0
            AirAsia_India = 0
            Vistara = 0
            Multiple_Airlines = 0

        elif(airline=='Air India'):
            IndiGo = 0
            GoAir = 0
            Air_India = 1 
            SpiceJet = 0
            AirAsia_India = 0
            Vistara = 0
            Multiple_Airlines = 0
            
        elif(airline=='SpiceJet'):
            IndiGo = 0
            GoAir = 0
            Air_India = 0 
            SpiceJet = 1
            AirAsia_India = 0
            Vistara = 0
            Multiple_Airlines = 0
            
        elif(airline=='AirAsia India'):
            IndiGo = 0
            GoAir = 0
            Air_India = 0 
            SpiceJet = 0
            AirAsia_India = 1
            Vistara = 0
            Multiple_Airlines = 0
            
        elif(airline=='Vistara'):
            IndiGo = 0
            GoAir = 0
            Air_India = 0 
            SpiceJet = 0
            AirAsia_India = 0
            Vistara = 1
            Multiple_Airlines = 0

        elif(airline=='Multiple Airlines'):
            IndiGo = 0
            GoAir = 0
            Air_India = 0 
            SpiceJet = 0
            AirAsia_India = 0
            Vistara = 0
            Multiple_Airlines = 1

        else:
            IndiGo = 0
            GoAir = 0
            Air_India = 0 
            SpiceJet = 0
            AirAsia_India = 0
            Vistara = 0
            Multiple_Airlines = 0

        # print(IndiGo,
        #     GoAir,
        #     Air_India,
        #     SpiceJet,
        #     AirAsia_India,
        #     Vistara,
        #     Multiple_Airlines)

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'IXM'):
            IXM = 1
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'GOI'):
            IXM = 0
            GOI = 1
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'AMD'):
            IXM = 0
            GOI = 0
            AMD = 1
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0
        elif (Source == 'ATQ'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 1
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'BLR'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 1
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'BBI'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 1
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0
        
        elif (Source == 'BDQ'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 1
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'BHO'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 1
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'BKB'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 1
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'BOM'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 1
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'CCJ'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 1
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'CCU'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 1
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'IXC'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 1
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'MAA'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 1
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'CJB'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 1
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'DED'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 1
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0
        elif (Source == 'DEL'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 1
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'GAU'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 1
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'GAY'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 1
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'HBX'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 1
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'HYD'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 1
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'IDR'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 1
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'IMF'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 1
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'ISK'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 1
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'IXL'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 1
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'SXR'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 1
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'IXR'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 1
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'JAI'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 1
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0
        elif (Source == 'CNN'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 1
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'LKO'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 1
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'IXE'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 1
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'NAG'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 1
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'PAT'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 1
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'PNQ'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 1
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'RPR'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 1
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'SHL'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 1
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'STV'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 1
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'TRV'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 1
            VNS = 0
            VGA = 0
            VTZ = 0

        elif (Source == 'VNS'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 1
            VGA = 0
            VTZ = 0

        elif (Source == 'VGA'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 1
            VTZ = 0

        elif (Source == 'VTZ'):
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 1

        else:
            IXM = 0
            GOI = 0
            AMD = 0
            ATQ = 0
            BLR = 0
            BBI = 0
            BDQ = 0
            BHO = 0
            BKB = 0
            BOM = 0
            CCJ = 0
            CCU = 0
            IXC = 0
            MAA = 0
            CJB = 0
            DED = 0
            DEL = 0
            GAU = 0
            GAY = 0
            HBX = 0
            HYD = 0
            IDR = 0
            IMF = 0
            ISK = 0
            IXL = 0
            SXR = 0
            IXR = 0
            JAI = 0
            CNN = 0
            LKO = 0
            IXE = 0
            NAG = 0
            PAT = 0
            PNQ = 0
            RPR = 0
            SHL = 0
            STV = 0
            TRV = 0
            VNS = 0
            VGA = 0
            VTZ = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination)
        Source = request.form["Destination"]
        if(Source == 'BLR'):
            d_BLR = 1
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0
        
        elif(Source == 'MAA'):
            d_BLR = 0
            d_MAA = 1
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'BOM'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 1
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'TRV'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 1
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'STV'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 1
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'VNS'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 1
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'HYD'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 1
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'KNU'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 1
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'ATQ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 1
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'DEL'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 1
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'CJB'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 1
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'AMD'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 1
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'BHO'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 1
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'GOI'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 1
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'UDR'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 1
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'COK'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 1
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'GAU'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 1
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXA'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 1
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXB'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 1
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXZ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 1
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'JLR'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 1
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'AGX'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 1
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'CCU'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 1
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'GOP'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 1
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXL'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 1
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'CCJ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 1
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'NAG'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 1
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'PNQ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 1
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'RAJ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 1
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'DIB'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 1
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'GAY'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 1
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IMF'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 1
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'SXR'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 1
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'LKO'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 1
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'JAI'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 1
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'HBX'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 1
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXE'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 1
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'PAT'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 1
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0
        
        elif(Source == 'IXC'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 1
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXR'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 1
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'VGA'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 1
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'DED'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 1
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IDR'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 1
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'TRZ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 1
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'BDQ'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 1
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'JDH'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 1
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'DIU'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 1
            d_IXU = 0
            d_SHL = 0

        elif(Source == 'IXU'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 1
            d_SHL = 0

        elif(Source == 'SHL'):
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 1

        else:
            d_BLR = 0
            d_MAA = 0
            d_BOM = 0
            d_TRV = 0
            d_STV = 0
            d_VNS = 0
            d_HYD = 0
            d_KNU = 0
            d_ATQ = 0
            d_DEL = 0
            d_CJB = 0 
            d_AMD = 0
            d_BHO = 0
            d_GOI = 0
            d_UDR = 0
            d_COK = 0
            d_GAU = 0
            d_IXA = 0
            d_IXB = 0
            d_IXZ = 0
            d_JLR = 0
            d_AGX = 0
            d_CCU = 0
            d_GOP = 0
            d_IXL = 0
            d_CCJ = 0
            d_NAG = 0
            d_PNQ = 0
            d_RAJ = 0
            d_DIB = 0
            d_GAY = 0
            d_IMF = 0
            d_SXR = 0
            d_LKO = 0
            d_JAI = 0
            d_HBX = 0
            d_IXE = 0
            d_PAT = 0
            d_IXC = 0
            d_IXR = 0
            d_VGA = 0
            d_DED = 0
            d_IDR = 0
            d_TRZ = 0
            d_BDQ = 0
            d_JDH = 0
            d_DIU = 0
            d_IXU = 0
            d_SHL = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        

        arr = [[
            Journey_day,
            day,
            Journey_month,
            Travel_Time,
            Total_stops,
            Price,
            Category,
            Dep_hour,
            Dep_min,
            AMD,	
            ATQ,
            BBI,
            BDQ,
            BHO,
            BKB,
            BLR,
            BOM,
            CCJ,
            CCU,
            CJB,
            CNN,
            DED,
            DEL,
            GAU,
            GAY,	
            GOI,
            HBX,
            HYD,	
            IDR,
            IMF,
            ISK,
            IXC,
            IXE,
            IXL,
            IXM,
            IXR,
            JAI,
            LKO,
            MAA,
            NAG,
            PAT,
            PNQ,
            RPR,
            SHL,
            STV,
            SXR,
            TRV,
            VGA,
            VNS,
            VTZ,
            Air_India,
            AirAsia_India,
            GoAir,
            IndiGo,
            Multiple_Airlines,
            SpiceJet,
            Vistara,
            d_AGX,	
            d_AMD,
            d_ATQ,	
            d_BDQ,	
            d_BHO,	
            d_BLR,	
            d_BOM,	
            d_CCJ,	
            d_CCU,	
            d_CJB,	
            d_COK,	
            d_DED,	
            d_DEL,	
            d_DIB,	
            d_DIU,	
            d_GAU,	
            d_GAY,	
            d_GOI,	
            d_GOP,	
            d_HBX,	
            d_HYD,	
            d_IDR,	
            d_IMF,	
            d_IXA,	
            d_IXB,	
            d_IXC,	
            d_IXE,	
            d_IXL,	
            d_IXR,	
            d_IXU,	
            d_IXZ,	
            d_JAI,	
            d_JDH,	
            d_JLR,	
            d_KNU,	
            d_LKO,	
            d_MAA,	
            d_NAG,	
            d_PAT,	
            d_PNQ,	
            d_RAJ,	
            d_SHL,	
            d_STV,	
            d_SXR,	
            d_TRV,	
            d_TRZ,	
            d_UDR,	
            d_VGA,	
            d_VNS,
        ]]
        
        new_df = pd.DataFrame(arr, columns = ['Out_Day','Out_Weekday','Out_Month','Out_Travel_Time','Out_Journey_Type','Price','sort',
                'Out_hour','Out_min','Out_Cities_AMD','Out_Cities_ATQ','Out_Cities_BBI','Out_Cities_BDQ','Out_Cities_BHO','Out_Cities_BKB',
                'Out_Cities_BLR','Out_Cities_BOM','Out_Cities_CCJ','Out_Cities_CCU','Out_Cities_CJB','Out_Cities_CNN','Out_Cities_DED',
                'Out_Cities_DEL','Out_Cities_GAU','Out_Cities_GAY','Out_Cities_GOI','Out_Cities_HBX','Out_Cities_HYD','Out_Cities_IDR',	
                'Out_Cities_IMF','Out_Cities_ISK','Out_Cities_IXC','Out_Cities_IXE','Out_Cities_IXL','Out_Cities_IXM','Out_Cities_IXR',
                'Out_Cities_JAI','Out_Cities_LKO','Out_Cities_MAA','Out_Cities_NAG','Out_Cities_PAT','Out_Cities_PNQ','Out_Cities_RPR',
                'Out_Cities_SHL','Out_Cities_STV','Out_Cities_SXR','Out_Cities_TRV','Out_Cities_VGA','Out_Cities_VNS','Out_Cities_VTZ',
                'Out_Airline_Air India','Out_Airline_AirAsia India','Out_Airline_GoAir','Out_Airline_IndiGo','Out_Airline_Multiple Airlines',
                'Out_Airline_SpiceJet','Out_Airline_Vistara','Dest_Cities_AGX','Dest_Cities_AMD','Dest_Cities_ATQ','Dest_Cities_BDQ',
                'Dest_Cities_BHO','Dest_Cities_BLR','Dest_Cities_BOM','Dest_Cities_CCJ','Dest_Cities_CCU','Dest_Cities_CJB','Dest_Cities_COK',
                'Dest_Cities_DED','Dest_Cities_DEL','Dest_Cities_DIB','Dest_Cities_DIU','Dest_Cities_GAU','Dest_Cities_GAY','Dest_Cities_GOI',
                'Dest_Cities_GOP','Dest_Cities_HBX','Dest_Cities_HYD','Dest_Cities_IDR','Dest_Cities_IMF','Dest_Cities_IXA','Dest_Cities_IXB',
                'Dest_Cities_IXC','Dest_Cities_IXE','Dest_Cities_IXL','Dest_Cities_IXR','Dest_Cities_IXU','Dest_Cities_IXZ','Dest_Cities_JAI',
                'Dest_Cities_JDH','Dest_Cities_JLR','Dest_Cities_KNU','Dest_Cities_LKO','Dest_Cities_MAA','Dest_Cities_NAG','Dest_Cities_PAT',
                'Dest_Cities_PNQ','Dest_Cities_RAJ','Dest_Cities_SHL','Dest_Cities_STV','Dest_Cities_SXR','Dest_Cities_TRV','Dest_Cities_TRZ',
                'Dest_Cities_UDR','Dest_Cities_VGA','Dest_Cities_VNS'])

        # num_col = ['Out_Day', 'Out_Weekday', 'Out_Month', 'Out_Travel_Time',
        #         'Out_Journey_Type', 'Price','sort', 'Out_hour', 'Out_min']

        # sc = StandardScaler()
        # new_df[num_col] = sc.fit_transform(new_df[num_col])
        # new_df[num_col] = sc.transform(new_df[num_col])

        # pca_final = pca.fit(new_df)

        # pca_final = IncrementalPCA(n_components = 38)
        # new_df_pca = pca_final.fit_transform(new_df)

        prediction = model.predict(new_df)

        output = round((prediction/(60))[0])

        arr_p = [[
            Journey_day,
            day,
            Journey_month,
            Travel_Time,
            Total_stops,
            Category,
            output,
            Dep_hour,
            Dep_min,
            AMD,	
            ATQ,
            BBI,
            BDQ,
            BHO,
            BKB,
            BLR,
            BOM,
            CCJ,
            CCU,
            CJB,
            CNN,
            DED,
            DEL,
            GAU,
            GAY,	
            GOI,
            HBX,
            HYD,	
            IDR,
            IMF,
            ISK,
            IXC,
            IXE,
            IXL,
            IXM,
            IXR,
            JAI,
            LKO,
            MAA,
            NAG,
            PAT,
            PNQ,
            RPR,
            SHL,
            STV,
            SXR,
            TRV,
            VGA,
            VNS,
            VTZ,
            Air_India,
            AirAsia_India,
            GoAir,
            IndiGo,
            Multiple_Airlines,
            SpiceJet,
            Vistara,
            d_AGX,	
            d_AMD,
            d_ATQ,	
            d_BDQ,	
            d_BHO,	
            d_BLR,	
            d_BOM,	
            d_CCJ,	
            d_CCU,	
            d_CJB,	
            d_COK,	
            d_DED,	
            d_DEL,	
            d_DIB,	
            d_DIU,	
            d_GAU,	
            d_GAY,	
            d_GOI,	
            d_GOP,	
            d_HBX,	
            d_HYD,	
            d_IDR,	
            d_IMF,	
            d_IXA,	
            d_IXB,	
            d_IXC,	
            d_IXE,	
            d_IXL,	
            d_IXR,	
            d_IXU,	
            d_IXZ,	
            d_JAI,	
            d_JDH,	
            d_JLR,	
            d_KNU,	
            d_LKO,	
            d_MAA,	
            d_NAG,	
            d_PAT,	
            d_PNQ,	
            d_RAJ,	
            d_SHL,	
            d_STV,	
            d_SXR,	
            d_TRV,	
            d_TRZ,	
            d_UDR,	
            d_VGA,	
            d_VNS,
        ]]
        
        new_df_p = pd.DataFrame(arr_p, columns = ['Out_Day','Out_Weekday','Out_Month','Out_Travel_Time','Out_Journey_Type','sort','Target_Var',
                'Out_hour','Out_min','Out_Cities_AMD','Out_Cities_ATQ','Out_Cities_BBI','Out_Cities_BDQ','Out_Cities_BHO','Out_Cities_BKB',
                'Out_Cities_BLR','Out_Cities_BOM','Out_Cities_CCJ','Out_Cities_CCU','Out_Cities_CJB','Out_Cities_CNN','Out_Cities_DED',
                'Out_Cities_DEL','Out_Cities_GAU','Out_Cities_GAY','Out_Cities_GOI','Out_Cities_HBX','Out_Cities_HYD','Out_Cities_IDR',	
                'Out_Cities_IMF','Out_Cities_ISK','Out_Cities_IXC','Out_Cities_IXE','Out_Cities_IXL','Out_Cities_IXM','Out_Cities_IXR',
                'Out_Cities_JAI','Out_Cities_LKO','Out_Cities_MAA','Out_Cities_NAG','Out_Cities_PAT','Out_Cities_PNQ','Out_Cities_RPR',
                'Out_Cities_SHL','Out_Cities_STV','Out_Cities_SXR','Out_Cities_TRV','Out_Cities_VGA','Out_Cities_VNS','Out_Cities_VTZ',
                'Out_Airline_Air India','Out_Airline_AirAsia India','Out_Airline_GoAir','Out_Airline_IndiGo','Out_Airline_Multiple Airlines',
                'Out_Airline_SpiceJet','Out_Airline_Vistara','Dest_Cities_AGX','Dest_Cities_AMD','Dest_Cities_ATQ','Dest_Cities_BDQ',
                'Dest_Cities_BHO','Dest_Cities_BLR','Dest_Cities_BOM','Dest_Cities_CCJ','Dest_Cities_CCU','Dest_Cities_CJB','Dest_Cities_COK',
                'Dest_Cities_DED','Dest_Cities_DEL','Dest_Cities_DIB','Dest_Cities_DIU','Dest_Cities_GAU','Dest_Cities_GAY','Dest_Cities_GOI',
                'Dest_Cities_GOP','Dest_Cities_HBX','Dest_Cities_HYD','Dest_Cities_IDR','Dest_Cities_IMF','Dest_Cities_IXA','Dest_Cities_IXB',
                'Dest_Cities_IXC','Dest_Cities_IXE','Dest_Cities_IXL','Dest_Cities_IXR','Dest_Cities_IXU','Dest_Cities_IXZ','Dest_Cities_JAI',
                'Dest_Cities_JDH','Dest_Cities_JLR','Dest_Cities_KNU','Dest_Cities_LKO','Dest_Cities_MAA','Dest_Cities_NAG','Dest_Cities_PAT',
                'Dest_Cities_PNQ','Dest_Cities_RAJ','Dest_Cities_SHL','Dest_Cities_STV','Dest_Cities_SXR','Dest_Cities_TRV','Dest_Cities_TRZ',
                'Dest_Cities_UDR','Dest_Cities_VGA','Dest_Cities_VNS'])

        prediction_p = model_p.predict(new_df_p)
        
        output_p = prediction_p[0]

        output = str(round(output/(24*60),2))
        output = output.split('.')

        a = int(output[0])
        b = int(output[1])
        if b > 24 and b < 49:
            b = b - 24
            a = a + 1
        elif b > 48 and b < 73:
            b = b - 48
            a = a + 2
        elif b > 72 and b < 97:
            b = b - 72
            a = a + 3
        elif b > 96 and b <= 100:
            b = b - 96
            a = a + 4
        l = [str(a), str(b)]
        l1 = '.'.join(l)
        l1 = float(l1)

        dateTimeObj = time.mktime(datetime.now().timetuple())
        c = datetime.now()
        d = timedelta(days = 20) 
        e = str(c + d)
        f = time.mktime(datetime.strptime(e,"%Y-%m-%d %H:%M:%S.%f").timetuple())
        g = time.mktime(datetime.strptime(date_dep,"%Y-%m-%dT%H:%M").timetuple())


        if(l1 < 0):
            return render_template('home.html',prediction_text="Buy your ticket now!")
        elif( g > dateTimeObj and g < f):
            return render_template('home.html',prediction_text="Buy your ticket now!")
        
        else:
            return render_template('home.html',prediction_text="You can wait and buy your ticket after {}Days {}hours and your approx. price will be {:.2f} INR".format(a, b, output_p))


    return render_template("home.html")

if __name__ == "__main__":
    app.run()
