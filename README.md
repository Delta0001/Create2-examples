# Create2
Friend gave me his iRobot Create2

Helpful links and notes:
- https://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf
- https://www.irobot.com/About-iRobot/STEM/Create-2/Projects.aspx
- Robot seems to create a lot of problems from the beginning when it comes to supplying an external device with power. Power will be supplied to PI using an external battery. I wish I didn't have to do this but I'd otherwise have to tap into the motor driver's power source. I'd like to keep soldering to a minimum with this project since I will be doing a lot more of that on my dual-wheel-drone project. 
- https://www.irobotweb.com/-/media/MainSite/PDFs/About/STEM/Create/BatteryPower.pdf
- https://www.irobotweb.com/-/media/MainSite/PDFs/About/STEM/Create/Create_2_to_5V_Logic.pdf
- Serial port's fuse supports 0.2A which pretty much restricts to serial communication. RX and TX lines are rated for 5V so I will stick to USB connection for communicating with the Pi. 
- https://www.irobotweb.com/-/media/MainSite/PDFs/About/STEM/Create/RaspberryPi_Tutorial.pdf
- http://blog.mindfront.net/2017/06/roomba-dashboard-cli-dashboard-for.html