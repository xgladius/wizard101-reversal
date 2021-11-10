# wizard101-reversal

#Client Events

Client events are how Wizard101 internally handles almost every action taken on the client. They are stored in an `std::list<Event> events` inside of the root `EventHandler` class.

Each client event is sent through `EventDispatcher::SendEvent` which takes an `std::string* event_name` and `EventArgs args`. This method searches through `events` inside of the root `EventHandler`, comparing each events' name to the provided `event_name`. When a match is found, it calls the events' callback.

Event struct:
```c
struct EventArg {
	// to be reversed
};

typedef void (*EventCallback)(EventArg arg);

struct Event {
	std::string* name;
	EventCallback callback;
};
```
