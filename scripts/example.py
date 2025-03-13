from procthor.generation import PROCTHOR10K_ROOM_SPEC_SAMPLER, HouseGenerator
from ai2thor.controller import Controller
from procthor.constants import PROCTHOR_INITIALIZATION

PROCTHOR_INITIALIZATION.pop("branch", None)

controller = Controller(
    quality="Low",
    commit_id="391b3fae4d4cc026f1522e5acf60953560235971",
    **PROCTHOR_INITIALIZATION,
)

house_generator = HouseGenerator(
    controller=controller, split="train", seed=42, 
    room_spec_sampler=PROCTHOR10K_ROOM_SPEC_SAMPLER
)
house, _ = house_generator.sample()
house.validate(house_generator.controller)

house.to_json("generated_house.json")
print(house.to_json())