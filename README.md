# moth-catcher-python-scripts

Python functions to control moth trap hardware


-------------
|controls.py|
-------------

trap_init()
----------------------
call at startup to set up input/outputs correctly and set interupts


trap_release()
----------------------
call to open hatch and release any moth in the trap


open_hatch(int <time>)
----------------------
run the servo to open the hatch for <time> seconds


close_hatch()
----------------------
run the servo to close the hatch, servo runs until the limit switch is hit (fully closed)


light_on(boolean)
----------------------
control the main moth attracting LEDs, True for on, False for off


fan_on(boolean)
----------------------
control the 12V fan, True to start the fan, False to stop
