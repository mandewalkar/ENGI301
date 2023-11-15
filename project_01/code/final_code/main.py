import screen
import touch
import os
import transcribe

if __name__ == '__main__':
    
    instruct = True
    begin = False
    start_rec = False
    stop_rec = False
    analysis = False
    
    
    try:
        import time
        delay = 2
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
                os.system('sudo python3 record.py')
                start_rec = False
                stop_rec = True
            if(stop_rec):
                print('touched, analyze')
                display.image('analysis.png')
                output = transcribe.analyze()
                ret = display.text_fit(output, 25)
                display.text(ret)
                time.sleep(delay)
                while(1):
                    if os.path.isfile('winner.txt'):
                        show = []
                        with open('winner.txt') as file:
                            for line in file:
                                show.append(line)
                        display.text('Prediction: ' + show[len(show)-1][19:len(show[len(show)-1])-2], justify=4, align=4)
                        break
                stop_rec = False
                analysis = True
                    
                
    except KeyboardInterrupt:
        print('Program ended by user.')

        