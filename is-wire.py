from is_wire.core import Channel, Subscription

# Connect to the broker
channel = Channel("amqp://guest:guest@localhost:5672")

# Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic="MyTopic.SubTopic")
# ... subscription.subscribe(topic="Other.Topic")

# Blocks forever waiting for one message from any subscription
message = channel.consume()
print(message)