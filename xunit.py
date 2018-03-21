class TestCase:
    def __init__(self, name):
        self.name= name
    def setUp(self):
        pass
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method= getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
    def tearDown(self):
        pass

class WasRun(TestCase):
    def setUp(self):
        self.WasRun= None
        self.log="setUp "
    def testMethod(self):
        self.WasRun =1
        self.log=self.log + "testMethod "
    def testBrokenMethod(self):
        raise Exception
    def tearDown(self):
        self.log=self.log + "tearDown "

class TestResult:
    def __init__(self):
        self.runCount= 0
        self.failureCount= 0
    def testStarted(self):
        self.runCount=self.runCount+1
    def testFailed(self):
        self.failureCount= self.failureCount + 1
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failureCount)

class TestSuite:
    def __init__(self, testClass=None):
        self.tests= []
        if(testClass != None):
            self.addTests(testClass)
    def add(self, test):
        self.tests.append(test)
    def addTests(self, testClass):
        testMethods=self.listTestMethod(testClass)
        for testcase in testMethods:
            self.add(testClass(testcase))
    def listTestMethod(self, className):
        return [func for func in dir(className) if callable(getattr(className, func)) and not func.startswith("__") and func.startswith("test")]
    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestCaseTest(TestCase):
    def __init__(self, name):
        print("TESTCASE: "+name)
        TestCase.__init__(self,name)
    def setUp(self):
        self.result= TestResult()
    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())
    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
    def testFailedResultFormatting(self):
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())
    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())
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
   
suite = TestSuite(TestCaseTest)
result= TestResult()
suite.run(result)
print result.summary()


