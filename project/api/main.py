from datetime import date

from fastapi import FastAPI
from pydantic import  BaseModel
app = FastAPI()

class  Player(BaseModel):
    id : int
    first_name : str
    last_name : str
    nickname : str | None = None
    date_of_birth : date
    height : int
    weight : int
    country : str | None = None
    position: str
    salary_per_year : float | None = None


player_1 = Player(
    id = 1,
    first_name="Steph",
    last_name="Curry",
    nickname="Chef Steph",
    date_of_birth="1986-06-25",
    position="PG",
    height=190,
    weight=86
)

player_2 = Player(
    id = 2,
    first_name="Klay",
    last_name="Thompson",
    date_of_birth="1986-06-25",
    position="SG",
    height=203,
    weight=95
)

list_of_players = [player_1,player_2]

@app.get("/players")
async def player_list():
    return list_of_players

@app.post("/players")
async def create_player(player: Player):
    player_dict = player.model_dump()
    today = date.today()
    age = today.year - player.date_of_birth.year

    # Check if birthday hasn't occurred yet this year
    if (today.month, today.day) < (player.date_of_birth.month, player.date_of_birth.day):
        age -= 1

    player_dict["age"] = age
    return player_dict

@app.get("/players/{player_id}")
async def player_detail(player_id: int):
    for player in list_of_players:
        if player.id == player_id:
            return player
    return {"Not found"}


