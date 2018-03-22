# xunit_example

## 작업목록

- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [x] 테스트 메서드가 실패하더라도 tearDown 호출하기 <2018.3.22 완료>
- [x] 테스트 여러 개 실행하기
- [x] 수집한 결과를 출력하기
- [x] WasRun에 로그 문자열 남기기
- [x] 실패한 테스트 보고하기
- [x] setUp 에러를 잡아서 보고하기 <2018.3.22 완료>
- [x] TestCase 클래스에서 TestSuite 생성하기 <2018.3.21 완료>

## 2018.3.20 작성

Test-Driven Development:ByExample, Kent Beck의 책 중 2 xUnit 예시를 따라 작성하고 실행해본 결과입니다. 이후 책에서는 소개되지 작업들을  구현해 볼 생각입니다

## 2018.3.21 작성

작업목록 중 'TestCase 클래스에서 TestSuite 생성하기' 를 해보려 했는데 작업 자체가 뭔지 이해가 잘안되었는데 누군가 먼저 풀어보신 분이 계셔서 참고해서 진행하였다.

* http://newy.tistory.com/entry/post-1  

태스크이해만하고 실제 작성은 제 나름대로 진행하여서 윗분의 결과물하고는 약간 상이한 부분이 있습니다. 자세한 부분은 커밋 로그를 참고해주세요.

오늘 작성된 테스트는 다음과 같습니다.

  ```python
      def testListTestMethod(self):
          method_list = TestSuite().listTestMethod(WasRun)
          actual_list= ""
          for method in method_list:
              actual_list += method + ","
          print actual_list
          assert("testBrokenMethod,testMethod," ==  actual_list)
      def testAutoSuite(self):
          suite= TestSuite(WasRun)
          suite.run(self.result)
          assert("2 run, 1 failed" == self.result.summary())
  ```

  오늘 작성된 코드는 다음과 같습니다.

  ```python
class TestSuite:
    def __init__(self, testClass=None):
        self.tests= []
        if(testClass != None):
            self.addTests(testClass)
    def addTests(self, testClass):
        testMethods=self.listTestMethod(testClass)
        for testcase in testMethods:
            self.add(testClass(testcase))
    def listTestMethod(self, className):
        return [func for func in dir(className) if callable(getattr(className, func)) and not func.startswith("__") and func.startswith("test")]
  ```
파이썬은 조금 생소하긴한데 Kent Beck 아저씨 말대로 xUnit을 만들어가면서 언어적특징을 배워가는 맛도 있긴 하네요!
  
## 2018.3.22 작성(한밤중)

잠자기전에 조금 작업해보았습니다. 작업한 것은 setUp이 실패하더라도 tearDown이 호출되게 하는 것입니다. 단순히 try 구문안으로 setUp을 포함시키는 것으로 간단히 해결하였습니다.
그리고 기존의 WasRun대신에 setUp이 실패할 테스트가 필요하여서 WasRunBroken을 생성하였습니다.

```python
    def testTearDownShouldCalledEvenIfSetupFailed(self):
        test= WasRunBroken("testMethod")
        test.run(self.result)
        assert("setUp tearDown " == test.log)
```

## 2018.3.22 작성(오후)

회사에서 머리식힐겸 작업을 했습니다. "setUp 에러를 잡아서 보고하기" 인데, 그렇게 어렵지 않고 지금 구현된 수준에서 테스트만 추가하였습니다.
그리고 몇가지 리팩터링도 하였구요. 아무래도 테스크를 제가 직접 뽑은게 아니고 책에 있는 내용을 하다보니 의도파악이 잘안되긴해서 맞게 한것인지는 모르겠네요.
앞으로는 Python에서 제공되는 unittest와 유사한 수준으로 구현을 해나가려고합니다. 현재 있는 태스크는 모두해버려서 일단 Python unittest에서 어떤것들이 되는지 사용해보고
태스크를 먼저 뽑아봐야겠습니다.

p.s. 참고로 VS code가지고 이작업을 하고 있는데 은근히 편하네요. 그전엔 Pycharm을 썼었는데.. 대체해볼만한듯합니다.

```python
    def testFailedResultEvenIfSetupFailed(self):
        suite= TestSuite(WasRunBroken)
        suite.run(self.result)
        assert("2 run, 2 failed" == self.result.summary())
```
