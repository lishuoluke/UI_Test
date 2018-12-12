#Chrome/Firefox/IE driver need to be put in the same directory

#The test is triggered by nosetest, trigger command:

nosetests --processes=5 nose_test_Annoucement.py nose_test_Dashboards.py nose_test_Home.py nose_test_Settings.py nose_test_Statistics.py --process-timeout=180 -v -s >result.txt 2>&1

#concurrent run 5 test case in one go, resul tin result.txt


