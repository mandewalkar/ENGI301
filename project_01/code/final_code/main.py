import screen
import touch

if __name__ == '__main__':
    
    instruct = True
    begin = False
    start_rec = False
    stop_rec = False
    analysis = False
    
    
    try:
        import time
        delay = 5
        touchscreen = touch.Touchscreen()
        print('init display')
        display = screen.SPI_Display()
        print('init image')
        display.image('help.png')
        time.sleep(delay)

    
        while (1):
            if (touchscreen.check_bottom_right() and instruct):
                print('touched, begin mode')
                display.image('begin.png')
                instruct = False
                begin = True
            if (touchscreen.check_middle() and begin):
                print('touched, record mode on')
                display.image('startRec.png')
                begin = False
                start_rec = True
            if (touchscreen.check_bottom_middle() and start_rec):
                print('touched, begin the recording')
                display.image('rec.png')
                start_rec = False
                stop_rec = True
            if(touchscreen.check_bottom_middle() and stop_rec):
                print('touched, analyze')
                display.image('analysis.png')
                stop_rec = False
                analysis = True
                    
                
    except KeyboardInterrupt:
        print('Program ended by user.')

        