import pytest
import gameplay.card_draw_discard_cycle as mod

CASES = [
    ("draw_discard_atomic", (1,)),
    ("rng_per_match_seed", (1,)),
    ("discard_by_id", (1,)),
    ("server_draw_authority", (1,)),
    ("reshuffle_before_draw", (1,)),
    ("snapshot_count_check", (1,)),
    ("draw", (1,)),
    ("discard", (1,)),
    ("reshuffle", (1,)),
    ("present", (1,)),
    ("validate_pile", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
