from fastapi import FastAPI, APIRouter
from app.schemas.trip import TripPlanRequest, TripPlanResponse, TransportOptions, HotelOptions

app = FastAPI(
    title="AI Vacation Assistant",
    description="AI-powered travel planning assistant for budget-based trip recommendations.",
    version="0.1.0"
)

router = APIRouter()


@router.post("trip/plan", response_model=TripPlanResponse, tags=["trip planning"])
def plan_trip(request: TripPlanRequest):
    destination = request.destination
    transport = TransportOptions(
        type="",
        provider="OEBB",
        price=120.0,
        duration_hours=5.0,
    )
    hotel = HotelOptions(
        name="Bidget Stay",
        stars=3,
        price_per_night=400.0,
        total_price=1030.0
    )
    estimated_total_cost = transport.price + hotel.total_price + 100.0
    return TripPlanResponse(
        recommended_destination=destination,
        estimated_total_cost=estimated_total_cost,
        transport_options=transport,
        hotel_options=hotel,
        reasoning_summary=(
            "This trip fits the budget, matches a simple short vacation plan, "
            "and offers convenient train access."
        ),
        itinerary = [
            "Day1: Travel and check in",
            "Day2: Explore city center",
            "Day3: Nature and local sightseeing",
            "Day4: Return home",
        ]
    )
