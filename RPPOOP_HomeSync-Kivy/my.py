from kivy.app import App
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import ujson

class MyApp(App):
    def build(self):
        # Load configuration from Firebase
        url = 'https://console.firebase.google.com/u/0/project/rppoophomesync/database/rppoophomesync-default-rtdb/data/~2F/led_state.json'
        headers = {'Content-type': 'application/json'}
        self.firebase_request = UrlRequest(url, on_success=self.on_success, on_error=self.on_error, req_headers=headers)

        # Set initial state of button based on configuration
        button = Button(text='Turn on LED', state='normal')
        button.bind(state=self.update_led_state)

        return button

    def on_success(self, request, data):
        # Set initial state of button and LED based on Firebase configuration
        button_state = 'down' if data['led_state'] == 'on' else 'normal'
        self.root.state = button_state
        self.update_led_state(self.root, button_state)

    def on_error(self, request, error):
        # Firebase request failed, use default configuration
        button_state = 'normal'
        self.root.state = button_state
        self.update_led_state(self.root, button_state)

    def update_led_state(self, button, state):
        # Send signal to Firebase to update LED state
        url = '<FIREBASE-URL>/led_state.json'
        headers = {'Content-type': 'application/json'}
        data = ujson.dumps({'led_state': 'on' if state == 'down' else 'off'})
        self.firebase_request = UrlRequest(url, on_success=None, on_error=None, req_headers=headers, req_body=data)

if __name__ == '__main__':
    MyApp().run()
