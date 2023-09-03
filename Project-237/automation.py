import time
from player import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = '**Drink your Water**',
            message = 'Drinking water helps to maintain the balance of body fluids',
            timeout = 10
        )
        
        time.sleep(60*30)