import pytest
from sample_class import TestAccount

def testDisplayVar1():
    test = TestAccount("test",1.0)
    assert TestAccount.displayVar1 == "Var 1:test"

def testDisplayVar2():
    test = TestAccount("asdf",1.0)
    assert TestAccount.displayVar2 == "Var2: 1.0"

def testIncrement():
    test = TestAccount("test",1.0)
    assert TestAccount.incrementVar2 == "Var2 is now: 2.0"

