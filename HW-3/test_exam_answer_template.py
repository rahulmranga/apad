import exam_answer as DroneSet
import inspect
import pytest_check as check

def test_answer():
    #Create object ds1 of class DroneSet
    ds1=DroneSet.DroneSet()
    #Write code to inpsect if DroneSet is member of the class DroneSet
    check.is_instance(ds1,DroneSet.DroneSet) # <1 points> Enter your code here>
    # Write code to check if DroneSet has a private attribute
    assert "_DroneSet__availability" or "_DroneSet__capacity" or "_DroneSet__checkOutQty" or "_DroneSet__checkOutId" in ds1.__dict__.keys()  # <1 points> Enter your code here>
    #Write code to test if the output of the get_availability method is equal to the capacity of 200
    assert ds1.get_availability()==200  # <1 points>Enter your code here>
    #Write code to test if the output of the check_out method is equal to 0 when you try to check out 20 units
    assert ds1.check_out(20)==0
    #Write code to test if the output of the get_availability method is equal to 180 now since you have checked out 20 units
    assert ds1.get_availability()==180 # <1 points>Enter your code here>
    #Write code to test if the output of the check_out method is equal to 1 when you try to check out 30 units
    assert ds1.check_out(30)==1# <1 points>Enter your code here>
    #Write code to test if the output of the get_availability method is equal to 150 now since you have checked out 30 units
    assert ds1.get_availability()==150 # <1 points>Enter your code here>
    #Write code to test if the output of the check_in method is equal to -1 (Error) if you try to checkin 25 units with checkOutID equal to 0
    assert ds1.check_in(0,25)==-1 # <1 points>Enter your code here>
    #Write code to test if the output of the check_in method is equal to 0 (No Error) if you try to checkin 20 units with checkOutID equal to 0
    assert ds1.check_in(0,20)==0 # <1 points>Enter your code here>
    #Write code to test if the output of the get_availability method is equal to 170 now since you have checked in 20 units
    assert ds1.get_availability()==170 # <1 points>Enter your code here>
    #Write code to test if the output of the check_in method is equal to 0 (No Error) if you try to checkin 30 units with checkOutID equal to 1
    assert ds1.check_in(1,30)==0# <1 points>Enter your code here>
    #Write code to test if the output of the get_availability method is equal to 200 now since you have checked out 30 units
    assert ds1.get_availability()==200 # <1 points>Enter your code here>
