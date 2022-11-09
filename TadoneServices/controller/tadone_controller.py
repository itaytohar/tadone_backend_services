from flask import Blueprint, request, Response
from flask_cors import CORS, cross_origin
from datetime import datetime, timezone
from decimal import Decimal
import json
import pandas as pd
from random import randrange
#from TadoneServices.dal.db_utils import DBUtil

tadone_controller = Blueprint("tadone_controller", __name__)


@tadone_controller.route("/services", methods=["GET"])
@cross_origin()
def getServices():
    try:
        lst = []
        lst.append({"id": 1, "desc": "ניקוי רכב", "avgHourPrice": 80, "populare": "true",
                   "tip": "השבוע חסכנו 184 שעות לאנשים בניקוי רכבים"})
        lst.append({"id": 2, "desc": "איסוף חבילה", "avgHourPrice": 30, "populare": "true",
                   "tip": "החודש אספנו 1793 חבילות ופינינו לאנשים מלאזמן לעשות כיף!"})
        lst.append({"id": 3, "desc": "שטיפת כלים", "avgHourPrice": 50, "populare": "false",
                   "tip": "החודש שטפנו כלים ל 236 משפחות מאושרות"})
        lst.append({"id": 4, "desc": "קיפול כביסה", "avgHourPrice": 60, "populare": "true",
                   "tip": "הידעתם? אנחנו מבזבזים כ 8 שעות בחודש בקיפול כביסה"})
        data_df = pd.DataFrame(lst)
        res = json.dumps(data_df.to_dict(orient="records"))
        #res = json.dumps(DBUtil().GetServices().to_dict(orient="records"))
        resCode = 200
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/services/request/<consumerId>", methods=["POST"])
@cross_origin()
def createServiceRequest(consumerId):
    try:
        #data = request.data

        res = json.dumps({"requestID": randrange(90000)})
        resCode = 201
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/providers/<serviceId>/providerDetails", methods=["GET"])
@cross_origin()
def serviceProvidersDetails(serviceId):
    try:
        #args = request.args
        #request_id = args["requestID"]
        # data = {'serviceProviders': [{"serviceProvider": {"id": "1", "name": "דין", "rating": 4.2, "about": "אני דין, וקיפול כביסה , אצלי תקבלו כביסה מקופלת כמו שצריך וביעילות מירבית", "friendsLike": [{"name": "אורי להב"}, {"name": "יפית שגב"}], "photosAndVideos": [{"id": "1", "url": "https://gcloud/store/photos/424-23-555324.png"}, {"id": "2", "url": "https://gcloud/store/videos/424-23-454411.wav"}], "reviews": [{"id": "1", "name": "יפה", "rating": 4, "remarks": "דור ביצע אצלי בבית עבודת קיפול כביסה מצויינת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "2", "name": "מיכאל", "rating": 5, "remarks": "דור ביצע עבודת קיפול כביסה מאסיבית, הגיע בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}, {
        #     "serviceProvider": {"id": "2", "name": "יעל", "rating": 4.8, "about": "אני יעל, בעלת שיטה חדשנית לקיפול כביסה זו המומחיות שלי, הכל יוצא מושלם", "friendsLike": [{"name": "אפי שמואלי"}, {"name": "עירית אלמליח"}], "photosAndVideos": [{"id": "3", "url": "https://gcloud/store/photos/225-23-555324.png"}, {"id": "4", "url": "https://gcloud/store/videos/586-23-23445.wav"}], "reviews": [{"id": "3", "name": "דודו", "rating": 5, "remarks": "יעל ביצעה אצלי בבית עבודת קיפול כביסה מטורפת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "4", "name": "שולה", "rating": 5, "remarks": "יעל ביצעה עבודת קיפול מדהימה , הגיעה בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}]}
        data = [
            {
                "id": 4,
                "name": "שמעון",
                "rating": "4.1",
                "about": "אני שמעון, יכול לקחת לכם את הרכב שלכם לשטיפה ולהחזיר לכם אותו כמו חדש",
                "serviceId": 1
            },
            {
                "id": 5,
                "name": "שמרית",
                "rating": "4.6",
                "about": "אני שמרית, סטודנטית וזקוקה לכסף, אשמח לקחת את רכבכם לשטיפה, מבטיחה שתהיו מרוצים",
                "serviceId": 1
            },
            {
                "id": 6,
                "name": "נועם",
                "rating": "4.9",
                "about": "אני נועם, רוצים שירות מהיר ויעיל? הגעתם לאדם הנכון",
                "serviceId": 1
            }
        ]
        res = json.dumps(data)

        # res = json.dumps(DBUtil().GetProvidersDetails(
        #     serviceId).to_dict(orient="records"), cls=DecimalEncoder)

        resCode = 200
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/providers/<providerId>/reviews", methods=["GET"])
@cross_origin()
def serviceProvidersReviews(providerId):
    try:
        #args = request.args
        #request_id = args["requestID"]
        # data = {'serviceProviders': [{"serviceProvider": {"id": "1", "name": "דין", "rating": 4.2, "about": "אני דין, וקיפול כביסה , אצלי תקבלו כביסה מקופלת כמו שצריך וביעילות מירבית", "friendsLike": [{"name": "אורי להב"}, {"name": "יפית שגב"}], "photosAndVideos": [{"id": "1", "url": "https://gcloud/store/photos/424-23-555324.png"}, {"id": "2", "url": "https://gcloud/store/videos/424-23-454411.wav"}], "reviews": [{"id": "1", "name": "יפה", "rating": 4, "remarks": "דור ביצע אצלי בבית עבודת קיפול כביסה מצויינת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "2", "name": "מיכאל", "rating": 5, "remarks": "דור ביצע עבודת קיפול כביסה מאסיבית, הגיע בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}, {
        #     "serviceProvider": {"id": "2", "name": "יעל", "rating": 4.8, "about": "אני יעל, בעלת שיטה חדשנית לקיפול כביסה זו המומחיות שלי, הכל יוצא מושלם", "friendsLike": [{"name": "אפי שמואלי"}, {"name": "עירית אלמליח"}], "photosAndVideos": [{"id": "3", "url": "https://gcloud/store/photos/225-23-555324.png"}, {"id": "4", "url": "https://gcloud/store/videos/586-23-23445.wav"}], "reviews": [{"id": "3", "name": "דודו", "rating": 5, "remarks": "יעל ביצעה אצלי בבית עבודת קיפול כביסה מטורפת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "4", "name": "שולה", "rating": 5, "remarks": "יעל ביצעה עבודת קיפול מדהימה , הגיעה בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}]}

        data = [
            {
                "id": 1,
                "providerId": 1,
                "name": "נעמה",
                "rating": 5,
                "remark": "דור מקפל כביסה בצורה יעילה, גם מהיר וגם מדוייק, ממש קיבלתי שירות מעולה וגם אדם אדיב ונחמד, ממליצה בחום"
            },
            {
                "id": 2,
                "providerId": 1,
                "name": "יניב",
                "rating": 4,
                "remark": "דור היה אצלי, קיפל 3 מכונות כביסה, עשה עבודה טובה, ממליץ"
            }
        ]
        res = json.dumps(data)

        # res = json.dumps(DBUtil().GetProvidersReviews(
        #     providerId).to_dict(orient="records"), cls=DecimalEncoder)

        resCode = 200
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/providers/<providerId>/friendsLikes", methods=["GET"])
@cross_origin()
def serviceProvidersFriendLikes(providerId):
    try:
        #args = request.args
        #request_id = args["requestID"]
        # data = {'serviceProviders': [{"serviceProvider": {"id": "1", "name": "דין", "rating": 4.2, "about": "אני דין, וקיפול כביסה , אצלי תקבלו כביסה מקופלת כמו שצריך וביעילות מירבית", "friendsLike": [{"name": "אורי להב"}, {"name": "יפית שגב"}], "photosAndVideos": [{"id": "1", "url": "https://gcloud/store/photos/424-23-555324.png"}, {"id": "2", "url": "https://gcloud/store/videos/424-23-454411.wav"}], "reviews": [{"id": "1", "name": "יפה", "rating": 4, "remarks": "דור ביצע אצלי בבית עבודת קיפול כביסה מצויינת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "2", "name": "מיכאל", "rating": 5, "remarks": "דור ביצע עבודת קיפול כביסה מאסיבית, הגיע בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}, {
        #     "serviceProvider": {"id": "2", "name": "יעל", "rating": 4.8, "about": "אני יעל, בעלת שיטה חדשנית לקיפול כביסה זו המומחיות שלי, הכל יוצא מושלם", "friendsLike": [{"name": "אפי שמואלי"}, {"name": "עירית אלמליח"}], "photosAndVideos": [{"id": "3", "url": "https://gcloud/store/photos/225-23-555324.png"}, {"id": "4", "url": "https://gcloud/store/videos/586-23-23445.wav"}], "reviews": [{"id": "3", "name": "דודו", "rating": 5, "remarks": "יעל ביצעה אצלי בבית עבודת קיפול כביסה מטורפת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "4", "name": "שולה", "rating": 5, "remarks": "יעל ביצעה עבודת קיפול מדהימה , הגיעה בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}]}

        # res = json.dumps(data)

        data = [
            {
                "id": 1,
                "providerId": 1,
                "name": "יריב"
            }
        ]
        res = json.dumps(data)

        # res = json.dumps(DBUtil().GetProvidersFriendLikes(
        #     providerId).to_dict(orient="records"), cls=DecimalEncoder)

        resCode = 200
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/providers/<providerId>/photosAndVideos", methods=["GET"])
@cross_origin()
def serviceProvidersPhotosAndVideos(providerId):
    try:
        #args = request.args
        #request_id = args["requestID"]
        # data = {'serviceProviders': [{"serviceProvider": {"id": "1", "name": "דין", "rating": 4.2, "about": "אני דין, וקיפול כביסה , אצלי תקבלו כביסה מקופלת כמו שצריך וביעילות מירבית", "friendsLike": [{"name": "אורי להב"}, {"name": "יפית שגב"}], "photosAndVideos": [{"id": "1", "url": "https://gcloud/store/photos/424-23-555324.png"}, {"id": "2", "url": "https://gcloud/store/videos/424-23-454411.wav"}], "reviews": [{"id": "1", "name": "יפה", "rating": 4, "remarks": "דור ביצע אצלי בבית עבודת קיפול כביסה מצויינת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "2", "name": "מיכאל", "rating": 5, "remarks": "דור ביצע עבודת קיפול כביסה מאסיבית, הגיע בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}, {
        #     "serviceProvider": {"id": "2", "name": "יעל", "rating": 4.8, "about": "אני יעל, בעלת שיטה חדשנית לקיפול כביסה זו המומחיות שלי, הכל יוצא מושלם", "friendsLike": [{"name": "אפי שמואלי"}, {"name": "עירית אלמליח"}], "photosAndVideos": [{"id": "3", "url": "https://gcloud/store/photos/225-23-555324.png"}, {"id": "4", "url": "https://gcloud/store/videos/586-23-23445.wav"}], "reviews": [{"id": "3", "name": "דודו", "rating": 5, "remarks": "יעל ביצעה אצלי בבית עבודת קיפול כביסה מטורפת, הגיע בזמן ולקח מחיר הוגן"}, {"id": "4", "name": "שולה", "rating": 5, "remarks": "יעל ביצעה עבודת קיפול מדהימה , הגיעה בזמן ולקח מחיר ממש טוב והכל במקצועיות גבוהה"}]}}]}

        # res = json.dumps(data)

        data = [
            {
                "id": 1,
                "providerId": 5,
                "url": "https://storage.cloud.google.com/providers_photos/providersServices/12.png"
            },
            {
                "id": 2,
                "providerId": 5,
                "url": "https://storage.cloud.google.com/providers_photos/providersServices/9.png"
            }
        ]
        res = json.dumps(data)

        # res = json.dumps(DBUtil().GetProvidersPhotosAndVideos(
        #     providerId).to_dict(orient="records"), cls=DecimalEncoder)

        resCode = 200
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/services/deal/", methods=["POST"])
@cross_origin()
def dealMatch():
    try:
        #data = request.data
        #choices = {1: "ok", 2: "busy"}
        status = "ok"  # choices.get(randrange(3), "ok")
        res = json.dumps(
            {"status": status, "tip": " נצלי את הזמן שהתפנה לכוס קפה עם חברה"})
        resCode = 201
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    response = response
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@tadone_controller.route("/consumers/<gender>/consumerDetails", methods=["GET"])
@cross_origin()
def serviceConsumerDetails(gender):
    try:
       # args = request.args
        #consumer_id = args["consumerID"]
        # data = {"consumer": {"id": consumerId, "name": "דין", "age": 42,
        #                      "address": "הרצל 76 אור יהודה", "photo": "https://gcloud/store/photos/424-23-555324.png"}}
        # res = json.dumps(data)
        if gender == '1':
            data = [
                {
                    "id": 1,
                    "name": "שרית",
                    "photo": "https://storage.cloud.google.com/providers_photos/customerPhotos/1.png",
                    "gender": 1
                }
            ]
        else:
            data = [
                {
                    "id": 2,
                    "name": "עודד",
                    "photo": "https://storage.cloud.google.com/providers_photos/customerPhotos/2.png",
                    "gender": 2
                }
            ]
        res = json.dumps(data)
        # res = json.dumps(DBUtil().GetConsumerDetails(
        #     gender).to_dict(orient="records"), cls=DecimalEncoder)

        resCode = 200
    except Exception as ex:
        # general error
        resCode = 500
    response = Response(res, resCode, mimetype='application/json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)
