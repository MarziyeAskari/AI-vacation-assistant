from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class TravelDates(BaseModel):
    start: date
    end: date

class Preferences(BaseModel):
   style: Optional[str] = Field(default="budget", examples=["budget"])
   interest:Optional[list[str]] = Field(default_factory=list, examples=["nature","quiet"])
   transport:Optional[list[str]] = Field(default_factory=list, examples=["train","flight"])


class TripPlanRequest(BaseModel):
    origin: str=Field(...,examples=["Vienna"])
    destination: str=Field(default=None,examples=["Europe"])
    budget:str=Field(gt=0,examples=[600])
    dates:TravelDates
    travelers:int=Field(gt=0,examples=[1])
    preferences:Optional[Preferences] = None

class TransportOptions(BaseModel):
    type:str
    provider:str
    price:float
    duration_hours:float

class HotelOptions(BaseModel):
    name:str
    stars:int
    price_per_night:float
    total_price:float

class TripPlanResponse(BaseModel):
   recommended_destination:str
   transport_options:TransportOptions
   hotel_options:HotelOptions
   estimated_total_cost:float
   reasoning_summary:str
   itinerary:list[str]
