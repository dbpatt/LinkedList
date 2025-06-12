class TrainCar:
    """
    Node class representing a single train car in our linked list.
    Each car holds cargo (data) and a connection to the next car.
    """
    def __init__(self, cargo):
        self.cargo = cargo      # What this car is carrying (the data)
        self.next_car = None    # The coupling to the next car (pointer)


class Train:
    """
    LinkedList class representing a train made of connected cars.

    Key Concepts:
    - Each train car (node) only knows about the next car
    - To find a specific car, we must walk through from the engine
    - Adding/removing cars involves changing the couplings (pointers)
    - The train can grow and shrink dynamically
    - We track both engine (head) and caboose (tail) for efficiency

    Time Complexities:
    - add_car (append): O(1) - we have direct access to the tail
    - insert_car: O(n) - must walk to insertion point
    - get_cargo: O(n) - must walk to the position
    - remove_car: O(n) - must walk to removal point
    - how_many_cars: O(1) - we track this separately
    - is_empty: O(1) - simple check
    """

    def __init__(self):
        """Initialize an empty train (no cars yet)"""
        self.engine = None    # The front of the train (head pointer)
        self.caboose = None   # The last car of the train (tail pointer)
        self.car_count = 0    # Track number of cars for O(1) size access

    def add_car(self, cargo):
        """
        Add a new car to the end of the train.

        Algorithm: Direct Tail Access - O(1)
        1. Create new train car
        2. If train is empty, make it both engine and caboose
        3. Otherwise, attach to caboose and update caboose pointer
        """
        new_car = TrainCar(cargo)

        # Edge case: empty train
        if self.engine is None:
            self.engine = new_car
            self.caboose = new_car
        else:
            # Attach to the current caboose
            self.caboose.next_car = new_car
            # Update caboose to point to the new last car
            self.caboose = new_car

        self.car_count += 1

    def insert_car(self, car_number, cargo):
        """
        Insert a new car at a specific position.

        Algorithm: Insertion with Pointer Manipulation
        1. Validate position
        2. Handle special case: inserting at front
        3. Handle special case: inserting at end (use add_car)
        4. Otherwise, walk to the car BEFORE insertion point
        5. Decouple, insert new car, recouple
        """
        if car_number < 0 or car_number > self.car_count:
            raise IndexError(f"Can't insert car at position {car_number}!")

        # Special case: inserting at the end
        if car_number == self.car_count:
            self.add_car(cargo)
            return

        new_car = TrainCar(cargo)

        # Special case: inserting at the front (new engine car)
        if car_number == 0:
            new_car.next_car = self.engine
            self.engine = new_car
            # If this was the only car, update caboose too
            if self.car_count == 0:
                self.caboose = new_car
        else:
            # Walk to the car BEFORE where we want to insert
            current_car = self.engine
            for i in range(car_number - 1):
                current_car = current_car.next_car

            # Insert: decouple, add new car, recouple
            new_car.next_car = current_car.next_car
            current_car.next_car = new_car

        self.car_count += 1

    def get_cargo(self, car_number):
        """
        Get the cargo from a specific car.

        Algorithm: Linear Search by Position
        1. Validate car number
        2. Walk through cars counting positions
        3. Return cargo when we reach the target
        """
        if car_number < 0 or car_number >= self.car_count:
            raise IndexError(f"No car at position {car_number}!")

        # Walk to the requested car
        current_car = self.engine
        for i in range(car_number):
            current_car = current_car.next_car

        return current_car.cargo

    def remove_car(self, car_number):
        """
        Remove a car from the train and return its cargo.

        Algorithm: Deletion with Pointer Manipulation
        1. Validate car number
        2. Handle special case: removing engine car
        3. Otherwise, walk to car BEFORE the one to remove
        4. Decouple the car by skipping over it
        5. Update caboose if we removed the last car
        """
        if car_number < 0 or car_number >= self.car_count:
            raise IndexError(f"No car to remove at position {car_number}!")

        # Special case: removing the only car
        if self.car_count == 1:
            removed_cargo = self.engine.cargo
            self.engine = None
            self.caboose = None
        # Special case: removing the engine car
        elif car_number == 0:
            removed_cargo = self.engine.cargo
            self.engine = self.engine.next_car
        else:
            # Walk to the car BEFORE the one we want to remove
            current_car = self.engine
            for i in range(car_number - 1):
                current_car = current_car.next_car

            # Decouple: skip over the car to remove
            removed_cargo = current_car.next_car.cargo
            current_car.next_car = current_car.next_car.next_car

            # Update caboose if we removed the last car
            if current_car.next_car is None:
                self.caboose = current_car

        self.car_count -= 1
        return removed_cargo

    def how_many_cars(self):
        """Return the number of cars in the train"""
        return self.car_count

    def is_empty(self):
        """Check if the train has no cars"""
        return self.car_count == 0

    def show_train(self):
        """
        Display the entire train structure.
        Useful for debugging and visualization.
        """
        if self.is_empty():
            print("No train cars!")
            return

        print("Engine", end="")
        current_car = self.engine
        while current_car is not None:
            print(f" -> [{current_car.cargo}]", end="")
            current_car = current_car.next_car
        print()  # New line at the end

    def __str__(self):
        """
        String representation of the train (toString equivalent).
        Returns a formatted string showing all cars.
        """
        if self.is_empty():
            return "[]"

        elements = []
        current_car = self.engine
        while current_car is not None:
            elements.append(str(current_car.cargo))
            current_car = current_car.next_car

        return "[" + " -> ".join(elements) + "]"

    def __iter__(self):
        """
        Make the train iterable so we can use 'for cargo in train'.
        Uses yield to return each car's cargo one at a time.
        """
        current_car = self.engine
        while current_car is not None:
            yield current_car.cargo
            current_car = current_car.next_car

# LinkedList Project Reflection Notes
#
# # Reflections on challenges faced and how they were resolved.
#
# What parts of the project did I get stuck on?
# - Understanding pointers - kept thinking of them as "containing" the next node instead of "pointing to" it
# - Off-by-one errors in insert/remove - wasn't sure when to stop at car_number vs car_number-1
# - Visualizing pointer manipulation - drawing the before/after states helped immensely
# - Why Linked List when arrays exist - had to understand the trade-offs
# - Forgetting to include a caboose in to include a reference to the tail of the linked-list.
#
# Why was I stuck?
# - Mental model issue - kept thinking sequentially like arrays instead of connections
# - Pointer arithmetic confusion - when to use current vs current.next vs current.next.next
# - Edge cases - empty list and single node cases behave differently
# - Abstraction difficulty - hard to think of memory addresses as "connections"
#
# What information did I need to get unblocked?
# - Train analogy - thinking of nodes as train cars with couplings made it click
# - Drawing diagrams - visualizing pointer changes step by step
# - Understanding that we need the node BEFORE for most operations
# - Edge case patterns - first node is always special, last node has next=None
# - Peer insight to remind me the tail needed a pointer as well.
#
# How did I know I needed that information?
# - Segmentation faults and None errors showed I was accessing non-existent nodes
# - Insert/remove were affecting wrong positions - indicated off-by-one errors
# - Couldn't explain why my code worked - meant I didn't truly understand
# - Tests passing but couldn't modify for new requirements
#
# How did I find that information?
# - Drew every operation step by step with boxes and arrows
# - Used print statements to trace pointer positions during traversal
# - Compared with real-world analogies (train cars, chain links)
# - Tested edge cases systematically (empty, single, two nodes)
# - Broke complex operations into smaller steps
#
