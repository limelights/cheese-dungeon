from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database or storage structure for demonstration
# events = [] 

@app.route('/')
def index():
    """Renders the main page displaying all upcoming events[cite: 4]."""
    # Pass your events list/query to the template: render_template('index.html', events=events)
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_event():
    """Handles the creation of a new event via form submission[cite: 2]."""
    if request.method == 'POST':
        host = request.form.get('host')
        event_name = request.form.get('event_name')
        when = request.form.get('when')
        
        # Add validation or database logic here...
        
        return redirect(url_for('index'))
        
    return render_template('create-event.html')

@app.route('/event/<int:event_id>')
def view_event(event_id):
    """Displays details for a specific event and its participants[cite: 3]."""
    # Fetch event by event_id from database...
    # event = get_event_by_id(event_id)
    return render_template('event-details.html') # Assuming template is named event.html or similar

@app.route('/event/<int:event_id>/signup', methods=['POST'])
def signup_event(event_id):
    """Handles participant sign-ups for a specific event[cite: 3]."""
    participant_name = request.form.get('participant_name')
    
    # Save participant linked to event_id...
    
    return redirect(url_for('view_event', event_id=event_id))

@app.route('/event/<int:event_id>/participant/<int:participant_id>/remove', methods=['POST'])
def remove_participant(event_id, participant_id):
    """Handles removing a participant from an event[cite: 3]."""
    # Delete participant logic here...
    
    return redirect(url_for('view_event', event_id=event_id))

if __name__ == '__main__':
    app.run(debug=True)

