from pymavlink import mavutil
import BroadcastManager

if __name__ == '__main__':

    # BroadcastManager.start_threads()

    the_connection = mavutil.mavlink_connection('udpin:0.0.0.0:14540')

    for i in range(0,10):
        the_connection.wait_heartbeat()
        print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))