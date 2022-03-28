# DS
### DataStrutcure Project

### Install Requirements
```bash
pip install virtualenv
mkdir venv
virtualenv -p python3.9.6 venv
source venv/bin/activate
pip install -r  requirements.txt
pip install -r  requirements-test.txt
```

### Test
    pytest teset
    pytest tests/unit
    pytest tests/functional

## run test
python -m unittest -v  tests/unit/LinkedListTest.py

## Venv
    python -m venv ./venv
    

## Learning Resources


## Binary Search Tree
    - can be used both as dictionary & priority queue
    - B-Trees good for maintaining databases on Secondary disk storage
    - InOrder: L,Root,R
    - PreOrder: Root,L,R
    - PostOrder: L,R,Root
    - Radix Trees are often called "Tries"
