
import unittest
from Diksha_Reports.usage_by_course import usage_by_course_system_testing
from Diksha_Reports.usage_by_textbook import usage_by_textbook_system_suite
from Diksha_Reports.content_course import content_course_system_suite
from Diksha_Reports.content_textbook import content_textbook_system_suite
from Diksha_TPD.TPD_Completion_percentage import completion_system_test
from Diksha_TPD.TPD_Course_Progress import lpd_content_system_test
from Diksha_TPD.TPD_Enrollment_completion import enrollment_system_test
from Diksha_TPD.TPD_Teacher_Percentage import lpd_percentage_system_test
from Health_Card_Index import health_card_system_test
from Periodic_Test_Reports.Pat_Heatchart import patheatchart_system_test
from Teacher_Attendance import teacher_attendance_system_testing
from get_dir import pwd
from Periodic_Test_Reports.pat_LO_Table import PAT_LO_Table_system_suite
from reuse_func import GetData
from HTMLTestRunner import HTMLTestRunner


class MyTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_issue01(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    patheatchart_system_test.cQube_heatchart_system_test
                    )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' PAT Heat chart  System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue02(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    PAT_LO_Table_system_suite.cQube_pat_lotable_system_test
                  )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' PAT LO Table System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue03(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                content_course_system_suite.cQube_content_course_system_suite)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content BY Course System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue04(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_textbook_system_suite.cQube_content_textbook_systemtest
                )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content By Textbook report System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue05(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_course_system_testing.cQube_diskha_course_system_report
                )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Course   System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue06(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_textbook_system_suite.cQube_usage_textbook_system_report
                )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Textbook   System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue07(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    lpd_content_system_test.cQube_lpdcontent_system_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By TPD Course   System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue08(self):

            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    lpd_percentage_system_test.cQube_lpdpercentage_system_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By TPD Percentage   System Test  ',
                verbosity=1,

            )
            runner1.run(system_test)
            outfile.close()

    def test_issue09(self):
        system_test = unittest.TestSuite()
        system_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                enrollment_system_test.cQube_enrollment_systemtest
            )
        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title=' Usage By TPD Enrollment/Completion   System Test  ',
            verbosity=1,

        )
        runner1.run(system_test)
        outfile.close()

    def test_issue10(self):
        system_test = unittest.TestSuite()
        system_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                completion_system_test.cQube_completion_percentage_system
            )
        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title=' Usage By TPD Percentage  System Test  ',
            verbosity=1,

        )
        runner1.run(system_test)
        outfile.close()

    def test_issue11(self):
        system_test = unittest.TestSuite()
        system_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                health_card_system_test.Health_card_system_test
            )
        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title=' Health card System Test  ',
            verbosity=1,

        )
        runner1.run(system_test)
        outfile.close()

    def test_issue12(self):
        system_test = unittest.TestSuite()
        system_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                teacher_attendance_system_testing.cQube_Teacher_Attendance_systemTest
            )
        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Teacher  Health System Test  ',
            verbosity=1,

        )
        runner1.run(system_test)
        outfile.close()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()