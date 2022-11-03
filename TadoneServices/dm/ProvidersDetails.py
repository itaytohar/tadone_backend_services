# from typing import List
# from typing import Any
# from dataclasses import dataclass


# @dataclass
# class FriendsLike:
#     name: str

#     @staticmethod
#     def from_dict(obj: Any) -> 'FriendsLike':
#         _name = str(obj.get("name"))
#         return FriendsLike(_name)


# @dataclass
# class PhotosAndVideo:
#     id: str
#     url: str

#     @staticmethod
#     def from_dict(obj: Any) -> 'PhotosAndVideo':
#         _id = str(obj.get("id"))
#         _url = str(obj.get("url"))
#         return PhotosAndVideo(_id, _url)


# @dataclass
# class Review:
#     id: str
#     name: str
#     rating: int
#     remarks: str

#     @staticmethod
#     def from_dict(obj: Any) -> 'Review':
#         _id = str(obj.get("id"))
#         _name = str(obj.get("name"))
#         _rating = int(obj.get("rating"))
#         _remarks = str(obj.get("remarks"))
#         return Review(_id, _name, _rating, _remarks)


# @dataclass
# class ProvidersDetails:
#     serviceProviders: List[ServiceProvider]

#     @staticmethod
#     def from_dict(obj: Any) -> 'Root':
#         _serviceProviders = [ServiceProvider.from_dict(
#             y) for y in obj.get("serviceProviders")]
#         return Root(_serviceProviders)


# @dataclass
# class ServiceProvider:
#     serviceProvider: ServiceProvider

#     @staticmethod
#     def from_dict(obj: Any) -> 'ServiceProvider':
#         _serviceProvider = ServiceProvider.from_dict(
#             obj.get("serviceProvider"))
#         return ServiceProvider(_serviceProvider)


# @dataclass
# class ServiceProvider2:
#     id: str
#     name: str
#     rating: float
#     about: str
#     friendsLike: List[FriendsLike]
#     photosAndVideos: List[PhotosAndVideo]
#     reviews: List[Review]

#     @staticmethod
#     def from_dict(obj: Any) -> 'ServiceProvider2':
#         _id = str(obj.get("id"))
#         _name = str(obj.get("name"))
#         _rating = float(obj.get("rating"))
#         _about = str(obj.get("about"))
#         _friendsLike = [FriendsLike.from_dict(
#             y) for y in obj.get("friendsLike")]
#         _photosAndVideos = [PhotosAndVideo.from_dict(
#             y) for y in obj.get("photosAndVideos")]
#         _reviews = [Review.from_dict(y) for y in obj.get("reviews")]
#         return ServiceProvider2(_id, _name, _rating, _about, _friendsLike, _photosAndVideos, _reviews)

# # Example Usage
# # jsonstring = json.loads(myjsonstring)
# # root = Root.from_dict(jsonstring)
