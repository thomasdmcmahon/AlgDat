from MyMap import MyMap
from SeparateChainingMap import SeparateChainingMap
from LinearProbingMap import LinearProbingMap
import hypothesis as hyp # type: ignore
import hypothesis.strategies as st # type: ignore

@hyp.given(st.lists(st.integers()))
@hyp.settings(max_examples=1000)
def test_hashmaps(keys):
    ds = SeparateChainingMap()
    dl = LinearProbingMap()
    reference = dict()

    for key in keys:
        ds[key] = 1
        dl[key] = 1
        reference[key] = 1
        ds_ks = set(k for k, v in ds)
        dl_ks = set(k for k, v in dl)
        reference_ks = set(reference.keys())
        assert ds_ks == dl_ks == reference_ks

    for key in keys:
        del ds[key]
        del dl[key]
        if key in reference_ks:
            del reference[key]
        ds_ks = set(k for k, v in ds)
        dl_ks = set(k for k, v in dl)
        reference_ks = set(reference.keys())
        assert ds_ks == dl_ks == reference_ks

test_hashmaps()
