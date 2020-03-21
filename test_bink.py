# pylint: skip-file
import pytest
import mock
from bink import BinkTest, ReadFileError
from io import StringIO


@pytest.fixture(scope='session')
def test_csv_data():
    return "Property Name,Property Address [1],Property  Address [2],Property Address [3],Property Address [4],Unit Name,Tenant Name,Lease Start Date,Lease End Date,Lease Years,Current Rent\nBeecroft Hill,Broad Lane,,,LS13,Beecroft Hill - Telecom App,Arqiva Services ltd,01 Mar 1994,28 Feb 2058,64,23950.00\nPotternewton Crescent,Potternewton Est Playing Field,,,LS7,Potternewton Est Playing Field,Arqiva Ltd,24 Jun 1999,23 Jun 2019,20,6600.00\nSeacroft Gate (Chase) - Block 2,Telecomms Apparatus,Leeds,,LS14,Seacroft Gate (Chase) block 2-Telecom App.,Vodafone Ltd.,30 Jan 2004,29 Jan 2029,25,12250.00\nQueenswood Heights,Queenswood Heights,Queenswood Gardens,Headingley,Leeds,Queenswood Hgt-Telecom App.,Vodafone Ltd,08 Nov 2004,07 Nov 2029,25,9500.00\nArmley - Burnsall Grange,Armley,LS13,,,Burnsall Grange CSR 37865,O2 (UK) Ltd,26 Jul 2007,25 Jul 2032,25,12000.00\nSeacroft Gate (Chase) - Block 2,Telecomms Apparatus,Leeds,,LS14,\"Seacroft Gate (Chase) - Block 2, WYK 0414\",Hutchinson3G Uk Ltd&Everything Everywhere Ltd,21 Aug 2007,20 Aug 2032,25,12750.00\nCottingley Towers,Leeds,,,LS11,Cottingley Towers-WYK0052,Everything Everywhere Ltd,28 Jan 2008,27 Jan 2018,10,12750.00\nPotternewton Heights - Tel App,Potternewton Heights,Potternewton Lne,Leeds,,Potternewton Heights,Everything Everywhere Ltd,04 Mar 2008,03 Mar 2018,10,12750.00\nGipton Gate West,Leeds,,,LS9,Gipton Gate West-WYK0021,Everything Everywhere Ltd & Hutchinson 3G UK,01 Apr 2008,31 Mar 2018,10,12750.00\nTheaker Lane,Burnsall Grange,Leeds,,LS12,Burnsall Grange - WYK0144,Everything Everywhere Ltd,29 Apr 2008,28 Apr 2018,10,12750.00\nGledhow Towers - Telecom App,Brackenwood Drive,Leeds,,,Gledhow Towers - WYK0188,Everything Everywhere Ltd & Hutchinson 3G UK,20 May 2008,19 May 2018,10,12750.00\nLovell Park Heights,Yeb,,,LS7,Lovell Park Heights-- WYK0207,Everything Everywhere Ltd,17 Jun 2008,16 Jun 2018,10,12750.00\nShakespeare Towers,,,,LS9,Shakespeare Towers ref 1704255985,EverythingEverywhere Ltd & Hutchinson3GUK Ltd,10 Jun 2009,09 Jun 2019,10,12750.00\nGrayson Heights,Eden Mount,Burley Park,Leeds,LS5,Grayson Heights LDS175   LS0029,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nOatland Towers,Little London,,Leeds,,Oatland Towers LDS133   99603,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,15296.63\nThe Heights East,Gamble Hill,Bramley,Leeds 12,,The Heights East LDS045   55032,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nThe Heights,Farrow Bank Gamble Hill,Leeds,,,Raynville Court LDS047   55035,Everything Everywhere Ltd&Hutchison 3G UK LTd,01 Aug 2009,31 Jul 2019,10,14730.08\nBarncroft Towers,Seacroft,Yeb Ref 10462,,LS14,Barncroft Towers - Site Ref LDS138   99632,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nQueens View,Seacroft,,,LS14,Queens View LDS232   LS0098,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,28327.09\nParkway Grange,Foundry Lane,Leeds,,LS14,Parkway Grange - Site Ref LDS134   99604,Everything Everywhere Ltd&Hutchsion 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nSeacroft Gate Block 1,Eastdean,Leeds,,,Seacroft Gate Block 1 LDS032   55007,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nCartmell Drive,Halton Moor,Leeds,,LS15,Lakeland Court Flats Cell LDS142   99925,Everything Everywhere Ltd&Hutchison 3G UK Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nNorman Towers (Telecom Appar),Spen Lane,Leeds,,LS16,Norman Towers LDS132 (Telecom Appar)   99448,Everything Everywhere Ltd&Hutchsion 3G Ltd,01 Aug 2009,31 Jul 2019,10,14730.08\nClayton Court,Fillingfir Drive,,Leeds,LS18,Clayton Court LDS198   LS0056,Everything Everywhere Ltd & Hutchison 3G Ltd,01 Aug 2009,31 Jul 2019,10,15296.63\nMeynell Heights,,,,LS11,Meynell Heights- Wyk0184,Everything Everywhere Ltd & Hutchinson 3G UK,03 Aug 2009,02 Aug 2019,10,12750.00\nLarkhill Road,Lidgett Towers,Larkhill Road,Leeds,,Lidgett Towers - Site ref 27874,Everything Everywhere Ltd&Hutchison 3G UK Ltd,05 Jul 2010,04 Jul 2020,10,13000.00\nMarlborough Towers,Marlborough Towers,Park Lane,Leeds,,Marlborough Towers-Telecom App 7942vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nQueenswood Drive - Telecom Site,Headingley,Leeds,LS6,,Queenswood Drive-Q'wood Ct building 19089o2,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nClayton Court,Fillingfir,,Leeds,,Clayton Court 11279vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nGledhow Towers - Telecom App,Brackenwood Drive,Leeds,,,Gledhow Towers - Telecom App (34909vf),Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nLarkhill Road,Lidgett Towers,Larkhill Road,Leeds,,Lidgett Towers - Telecom App 3420vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nGipton Gate East,Oaktree Drive,,,,Gipton Gate East 23201vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nThe Heights East,Armley,Leeds,,LS12,The Heights East- 4797o2,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nBurnsall Gardens,Theaker Lane,,,,Burnsall Gardens - Cell No 23144vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,17000.00\nPoplar Mount,Armley,,,LS13,Poplar Mount Telecom Site 34884vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nBarncroft Court,Seacroft,Yeb Ref 10463,,LS14,Barncroft Court 34196o2,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nBarncroft Grange,Boggart Hill Drive,Seacroft,Leeds,LS14,Barncroft Grange Site 10639vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,17000.00\nBailey Lane,Baileys Lane,Leeds,,,\"Baileys Towers, Bailey Lane Ref 33420o2\",Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nSherburn Court,Mill Green,,Leeds,,Sherburn Court CSR 16878o2,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nCartmell Drive,Halton Moor,Leeds,,LS15,Lakeland Court Cell No 35649o2,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\nNorman Towers (Telecom Appar),Spen Lane,Leeds,,LS16,Norman Towers (Telecom Appar) 1701o2,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,22500.00\nKing Lane,Leafield Towers,Leeds,,LS16,Leafield Towers - Cell 5516vf,Cornerstone Telecommunications Infrastructure,31 Mar 2015,30 Mar 2030,15,15000.00\n"


class TestBinkTest():

    def test_initialisation(self):
        # Just a basic test to test the plumbing of the test to the classx
        bink_test = BinkTest(filename='testname.csv')
        assert bink_test.filename == 'testname.csv'
        assert not bink_test.data

    @pytest.mark.parametrize('option, expected_exception', [(1, ReadFileError),
                                                            (2, ReadFileError),
                                                            (3, ReadFileError),
                                                            (4, ReadFileError),
                                                            ('test', ValueError),
                                                            (5, ValueError)])
    def test_process_user_input_no_data(self, option, expected_exception):
        # Create the object
        bink_test = BinkTest(filename='testname.csv')

        # Test the return
        assert not bink_test.data
        if expected_exception:
            with pytest.raises(expected_exception):
                bink_test.process_user_input(option)
        else:
            bink_test.process_user_input(option)

    @pytest.mark.parametrize('option, expected_exception', [(1, None),
                                                            (2, None),
                                                            (3, None),
                                                            (4, None),
                                                            ('test', ValueError),
                                                            (5, ValueError)])
    def test_process_user_input_with_data(self, test_csv_data, option, expected_exception):
        # Create the object
        bink_test = BinkTest(filename='testname.csv')

        # Mock the return of open to inject a StringIO object rather than a file object
        f = StringIO(test_csv_data)
        with mock.patch('bink.open', return_value=f):
            if expected_exception:
                with pytest.raises(expected_exception):
                    bink_test.process_user_input(option)
            else:
                bink_test.process_user_input(option)
                assert bink_test.data

    def test_user_option_1(self, test_csv_data):
        # Create the object
        bink_test = BinkTest(filename='testname.csv')

        # Mock the return of open to inject a StringIO object rather than a file object
        f = StringIO(test_csv_data)
        with mock.patch('bink.open', return_value=f):
            with mock.patch('bink.BinkTest.print_container') as mock_print:
                bink_test.process_user_input(1)
                assert bink_test.data
                result_list = []
                result_list.append(bink_test.data[1])
                result_list.append(bink_test.data[3])
                result_list.append(bink_test.data[4])
                result_list.append(bink_test.data[2])
                result_list.append(bink_test.data[5])
                mock_print.assert_called_with(result_list)

    def test_user_option_2(self, test_csv_data):
        # Create the object
        bink_test = BinkTest(filename='testname.csv')

        # Mock the return of open to inject a StringIO object rather than a file object
        f = StringIO(test_csv_data)
        with mock.patch('bink.open', return_value=f):
            with mock.patch('bink.BinkTest.print_container') as mock_print:
                bink_test.process_user_input(2)
                assert bink_test.data
                result_list = []
                result_list.append(bink_test.data[2])
                result_list.append(bink_test.data[3])
                result_list.append(bink_test.data[4])
                result_list.append(bink_test.data[5])
                mock_print.assert_called_with(result_list)

    def test_user_option_3(self, test_csv_data):
        # Create the object
        bink_test = BinkTest(filename='testname.csv')

        # Mock the return of open to inject a StringIO object rather than a file object
        f = StringIO(test_csv_data)
        with mock.patch('bink.open', return_value=f):
            with mock.patch('bink.BinkTest.print_container') as mock_print:
                bink_test.process_user_input(3)
                assert bink_test.data
                out_dict = {'Arqiva Ltd': 1,
                            'Arqiva Services ltd': 1,
                            'Cornerstone Telecommunications Infrastructure': 16,
                            'Everything Everywhere Ltd': 4,
                            'Everything Everywhere Ltd & Hutchinson 3G UK': 3,
                            'Everything Everywhere Ltd & Hutchison 3G Ltd': 1,
                            'Everything Everywhere Ltd&Hutchison 3G UK LTd': 1,
                            'Everything Everywhere Ltd&Hutchison 3G UK Ltd': 8,
                            'Everything Everywhere Ltd&Hutchsion 3G Ltd': 1,
                            'Everything Everywhere Ltd&Hutchsion 3G UK Ltd': 1,
                            'EverythingEverywhere Ltd & Hutchinson3GUK Ltd': 1,
                            'Hutchinson3G Uk Ltd&Everything Everywhere Ltd': 1,
                            'O2 (UK) Ltd': 1,
                            'Vodafone Ltd': 1,
                            'Vodafone Ltd.': 1}

                mock_print.assert_called_with(out_dict, headers=['Tenant Name', 'Count'])

    def test_user_option_4(self, test_csv_data):
        # Create the object
        bink_test = BinkTest(filename='testname.csv')

        # Mock the return of open to inject a StringIO object rather than a file object
        f = StringIO(test_csv_data)
        with mock.patch('bink.open', return_value=f):
            with mock.patch('bink.BinkTest.print_container') as mock_print:
                bink_test.process_user_input(4)
                assert bink_test.data
                result_list = []
                result_list.append(bink_test.data[1])
                result_list.append(bink_test.data[2])
                result_list.append(bink_test.data[3])
                result_list.append(bink_test.data[4])
                result_list.append(bink_test.data[5])
                mock_print.assert_called_with(result_list)
