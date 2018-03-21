# xunit_example
## 작업목록
- [x] 테스트 메서드 호출하기
- [x] 먼저 setUp 호출하기
- [x] 나중에 tearDown 호출하기
- [ ] 테스트 메서드가 실패하더라도 tearDown 호출하기
- [x] 테스트 여러 개 실행하기
- [x] 수집한 결과를 출력하기
- [x] WasRun에 로그 문자열 남기기
- [x] 실패한 테스트 보고하기
- [ ] setUp 에러를 잡아서 보고하기
- [x] TestCase 클래스에서 TestSuite 생성하기 <2018.3.21 완료>

## 2018.3.20 작성
Test-Driven Development:ByExample, Kent Beck의 책 중 2 xUnit 예시를 따라 작성하고 실행해본 결과입니다  
이후 책에서는 소개되지 작업들을  구현해 볼 생각입니다

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