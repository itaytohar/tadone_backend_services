from typing import List
from TadoneServices.dm.base import session_factory
from TadoneServices.dm.data_sources import (
    services,
    providers_details_vw,
    providers_reviews,
    providers_photos_and_videos,
    providers_friends_likes,
    consumers_details,
)
from sqlalchemy import or_
import pandas as pd
import threading

data_src_session = session_factory()

lock = threading.Lock()


class DBUtil:

    def GetServices(self):
        try:

            data: List[services] = []
            base_query = data_src_session.query(services)
            data = base_query.all()

        except Exception as ex:
            print(ex)
        finally:
            data_src_session.close()

        return self.__generate_services_data_dataframe_From_db_result__(data)

    # @elasticapm.capture_span()

    def __generate_services_data_dataframe_From_db_result__(
        self, data: List[services]
    ):
        data_df = pd.DataFrame(
            columns=["id", "desc", "avgHourPrice", "populare", "tip"])

        lst = []
        for item in data:
            new_row = {
                "id": item.id,
                "desc": item.desc,
                "avgHourPrice": item.avgHourPrice,
                "populare": item.populare,
                "tip": item.tip
            }
            lst.append(new_row)

        data_df = pd.DataFrame(lst)

        return data_df

    def GetProvidersDetails(self, service_id: None):
        try:

            data: List[providers_details_vw] = []
            base_query = data_src_session.query(providers_details_vw)
            base_query = base_query.filter(
                or_(
                    providers_details_vw.serviceId.is_(None),
                    providers_details_vw.serviceId == service_id,
                )
            )
            data = base_query.all()

        except Exception as ex:
            print(ex)
        finally:
            data_src_session.close()

        return self.__generate_providers_data_dataframe_From_db_result__(data)

    def __generate_providers_data_dataframe_From_db_result__(
        self, data: List[providers_details_vw]
    ):
        data_df = pd.DataFrame(
            columns=["id", "name", "rating", "about", "serviceId", "url"])

        lst = []
        for item in data:
            new_row = {
                "id": item.id,
                "name": item.name,
                "rating": item.rating,
                "about": item.about,
                "serviceId": item.serviceId,
                "url": item.url,
            }
            lst.append(new_row)

        data_df = pd.DataFrame(lst)

        return data_df

    def GetProvidersReviews(self, provider_id: None):
        try:

            data: List[providers_reviews] = []
            base_query = data_src_session.query(providers_reviews)
            base_query = base_query.filter(
                or_(
                    providers_reviews.providerId.is_(None),
                    providers_reviews.providerId == provider_id,
                )
            )
            data = base_query.all()

        except Exception as ex:
            print(ex)
        finally:
            data_src_session.close()

        return self.__generate_providers_reviews_data_dataframe_From_db_result__(data)

    def __generate_providers_reviews_data_dataframe_From_db_result__(
        self, data: List[providers_reviews]
    ):
        data_df = pd.DataFrame(
            columns=["id", "providerId", "name", "rating", "remark"])

        lst = []
        for item in data:
            new_row = {
                "id": item.id,
                "providerId": item.providerId,
                "name": item.name,
                "rating": item.rating,
                "remark": item.remark,
            }
            lst.append(new_row)

        data_df = pd.DataFrame(lst)

        return data_df

    def GetProvidersPhotosAndVideos(self, provider_id: None):
        try:

            data: List[providers_photos_and_videos] = []
            base_query = data_src_session.query(providers_photos_and_videos)
            base_query = base_query.filter(
                or_(
                    providers_photos_and_videos.providerId.is_(None),
                    providers_photos_and_videos.providerId == provider_id,
                )
            )
            data = base_query.all()

        except Exception as ex:
            print(ex)
        finally:
            data_src_session.close()

        return self.__generate_providers_photos_and_videos_data_dataframe_From_db_result__(data)

    def __generate_providers_photos_and_videos_data_dataframe_From_db_result__(
        self, data: List[providers_photos_and_videos]
    ):
        data_df = pd.DataFrame(
            columns=["id", "providerId", "url"])

        lst = []
        for item in data:
            new_row = {
                "id": item.id,
                "providerId": item.providerId,
                "url": item.url,
            }
            lst.append(new_row)

        data_df = pd.DataFrame(lst)

        return data_df

    def GetProvidersFriendLikes(self, provider_id: None):
        try:

            data: List[providers_friends_likes] = []
            base_query = data_src_session.query(providers_friends_likes)
            base_query = base_query.filter(
                or_(
                    providers_friends_likes.providerId.is_(None),
                    providers_friends_likes.providerId == provider_id,
                )
            )
            data = base_query.all()

        except Exception as ex:
            print(ex)
        finally:
            data_src_session.close()

        return self.__generate_providers_friends_likes_data_dataframe_From_db_result__(data)

    def __generate_providers_friends_likes_data_dataframe_From_db_result__(
        self, data: List[providers_friends_likes]
    ):
        data_df = pd.DataFrame(
            columns=["id", "providerId", "name"])

        lst = []
        for item in data:
            new_row = {
                "id": item.id,
                "providerId": item.providerId,
                "name": item.name,
            }
            lst.append(new_row)

        data_df = pd.DataFrame(lst)

        return data_df

    def GetConsumerDetails(self, gender: None):
        try:

            data: List[consumers_details] = []
            base_query = data_src_session.query(consumers_details)
            base_query = base_query.filter(
                or_(
                    consumers_details.gender.is_(None),
                    consumers_details.gender == gender,
                )
            )
            data = base_query.all()

        except Exception as ex:
            print(ex)
        finally:
            data_src_session.close()

        return self.__generate_consumer_details_data_dataframe_From_db_result__(data)

    def __generate_consumer_details_data_dataframe_From_db_result__(
        self, data: List[consumers_details]
    ):
        data_df = pd.DataFrame(
            columns=["id", "name", "photo", "gender"])

        lst = []
        for item in data:
            new_row = {
                "id": item.id,
                "name": item.name,
                "photo": item.photo,
                "gender": item.gender,
            }
            lst.append(new_row)

        data_df = pd.DataFrame(lst)

        return data_df

# def GetProvidersFullDetails(self, service_id: None):
#     try:

#         data: List[providers_details_vw] = []
#         base_query = data_src_session.query(providers_details_vw)
#         base_query = base_query.filter(
#             or_(
#                 providers_details_vw.serviceId.is_(None),
#                 providers_details_vw.serviceId == service_id,
#             )
#         )
#         data = base_query.all()

#     except Exception as ex:
#         print(ex)
#     finally:
#         data_src_session.close()
#     res: List[providers_details_vw] = []
#     full_res: List[providers_full_details] = []
#     fd = providers_full_details
#     res = self.__generate_providers_data_dataframe_From_db_result__(data)
#     index = 0
#     for item in data:
#         index = index + 1
#         fd.providerID = item.id,
#         fd.name = item.name,
#         fd.rating = item.rating,
#         fd.about = item.about,
#         fd.serviceId = item.serviceId,

#         data2: List[providers_reviews] = []
#         base_query2 = data_src_session.query(providers_reviews)
#         base_query2 = base_query2.filter(
#             or_(
#                 providers_reviews.providerId.is_(None),
#                 providers_reviews.providerId == item.id,
#             )
#         )
#         data2 = base_query2.all()
#         res2: List[providers_reviews]
#         res2 = self.__generate_providers_reviews_data_dataframe_From_db_result__(
#             data2)
#         fd.reviews = data2

#         full_res.insert(index, fd)

#         # data_df = pd.DataFrame(
#         #     columns=["providerId", "name", "rating", "about", "serviceId", "reviews"])
#         #data_df = pd.DataFrame(full_res)
#     return full_res
