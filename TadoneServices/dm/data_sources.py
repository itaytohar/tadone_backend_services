# from sqlalchemy import Column, BigInteger, String, SmallInteger, Date, Boolean, Numeric
# from TadoneServices.dm.base import Base


# class services(Base):
#     __tablename__ = "services"
#     id = Column(
#         BigInteger,
#         primary_key=True,
#         nullable=False,
#     )
#     desc = Column(String, nullable=False)
#     avgHourPrice = Column(Numeric, nullable=False)
#     populare = Column(Boolean, nullable=False)
#     tip = Column(String, nullable=False)


# # class providers_full_details():
# #     def __init__(self, id, name, rating, about, serviceId, reviews):
# #         self.id = id,
# #         self.name = name,
# #         self.rating = rating,
# #         self.about = about,
# #         self.serviceId = serviceId,
# #         self.reviews = reviews

# class consumers_details(Base):
#     __tablename__ = "consumers"
#     id = Column(
#         "id",
#         BigInteger,
#         primary_key=True,
#         nullable=False,
#     )
#     name = Column(String, nullable=False)
#     photo = Column(String, nullable=False)
#     gender = Column(SmallInteger, nullable=False)


# class providers_details_vw(Base):
#     __tablename__ = "providers_details_vw"
#     id = Column(
#         "id",
#         BigInteger,
#         primary_key=True,
#         nullable=False,
#     )
#     name = Column(String, nullable=False)
#     rating = Column(Numeric, nullable=False)
#     about = Column(String, nullable=False)
#     serviceId = Column(BigInteger, nullable=False)


# class providers_reviews(Base):
#     __tablename__ = "providers_reviews"
#     id = Column(
#         "id",
#         BigInteger,
#         primary_key=True,
#         nullable=False,
#     )
#     providerId = Column(BigInteger, nullable=False)
#     name = Column(String, nullable=False)
#     rating = Column(Numeric, nullable=False)
#     remark = Column(String, nullable=False)


# class providers_friends_likes(Base):
#     __tablename__ = "providers_friends_likes"
#     id = Column(
#         "id",
#         BigInteger,
#         primary_key=True,
#         nullable=False,
#     )
#     providerId = Column(BigInteger, nullable=False)
#     name = Column(String, nullable=False)


# class providers_photos_and_videos(Base):
#     __tablename__ = "providers_photos_and_videos"
#     id = Column(
#         "id",
#         BigInteger,
#         primary_key=True,
#         nullable=False,
#     )
#     providerId = Column(BigInteger, nullable=False)
#     url = Column(String, nullable=False)
