from main import Train

def test_basic_operations():
    """Test basic add, get, and size operations"""
    print("=== Testing Basic Operations ===")
    train = Train()

    # Test empty train
    print(f"Empty train: {train}")
    print(f"Is empty: {train.is_empty()}")
    print(f"Car count: {train.how_many_cars()}")

    # Add some cars
    train.add_car("Passengers")
    train.add_car("Dining")
    train.add_car("Cargo")

    print(f"\nAfter adding 3 cars: {train}")
    print(f"Car count: {train.how_many_cars()}")
    print(f"Is empty: {train.is_empty()}")

    # Test get
    print(f"\nCar 0: {train.get_cargo(0)}")
    print(f"Car 1: {train.get_cargo(1)}")
    print(f"Car 2: {train.get_cargo(2)}")

    # Test error handling
    try:
        train.get_cargo(3)
    except IndexError as e:
        print(f"Expected error: {e}")

def test_insert_operations():
    """Test inserting cars at various positions"""
    print("\n=== Testing Insert Operations ===")
    train = Train()

    # Build initial train
    train.add_car("First")
    train.add_car("Third")
    print(f"Initial: {train}")

    # Insert in middle
    train.insert_car(1, "Second")
    print(f"After inserting 'Second' at position 1: {train}")

    # Insert at front
    train.insert_car(0, "Engine")
    print(f"After inserting 'Engine' at position 0: {train}")

    # Insert at end
    train.insert_car(4, "Caboose")
    print(f"After inserting 'Caboose' at end: {train}")

    # Test error handling
    try:
        train.insert_car(10, "Invalid")
    except IndexError as e:
        print(f"Expected error: {e}")

def test_remove_operations():
    """Test removing cars from various positions"""
    print("\n=== Testing Remove Operations ===")
    train = Train()

    # Build train with numbers
    for i in range(5):
        train.add_car(i * 10)

    print(f"Initial train: {train}")

    # Remove from middle
    removed = train.remove_car(2)
    print(f"Removed car 2 (value: {removed}): {train}")

    # Remove from front
    removed = train.remove_car(0)
    print(f"Removed car 0 (value: {removed}): {train}")

    # Remove from end
    removed = train.remove_car(train.how_many_cars() - 1)
    print(f"Removed last car (value: {removed}): {train}")

    # Test error handling
    try:
        train.remove_car(10)
    except IndexError as e:
        print(f"Expected error: {e}")

def test_edge_cases():
    """Test edge cases and special scenarios"""
    print("\n=== Testing Edge Cases ===")
    train = Train()

    # Single element operations
    train.add_car("Only")
    print(f"Single car train: {train}")

    removed = train.remove_car(0)
    print(f"After removing only car (value: {removed}): {train}")
    print(f"Is empty: {train.is_empty()}")

    # Insert into empty
    train.insert_car(0, "First")
    print(f"Insert into empty train: {train}")

    # Many rapid operations
    print("\nRapid operations test:")
    for i in range(3):
        train.add_car(f"Car{i}")
    train.show_train()

    train.insert_car(2, "Inserted")
    train.show_train()

    train.remove_car(1)
    train.show_train()

def test_iterator():
    """Test the iterator functionality"""
    print("\n=== Testing Iterator ===")
    train = Train()

    # Add different types of cargo
    cargo_list = ["Passengers", "Mail", "Packages", "Fuel", "Supplies"]
    for cargo in cargo_list:
        train.add_car(cargo)

    print(f"Train contents: {train}")

    print("\nIterating with for loop:")
    for cargo in train:
        print(f"  - {cargo}")

    print("\nProcessing with iterator:")
    manifest = []
    for cargo in train:
        manifest.append(f"[{cargo}]")
    print(f"Manifest: {', '.join(manifest)}")

def test_mixed_data_types():
    """Test with various data types as cargo"""
    print("\n=== Testing Mixed Data Types ===")
    train = Train()

    # Add different types
    train.add_car("String cargo")
    train.add_car(42)
    train.add_car(3.14)
    train.add_car(["List", "of", "items"])
    train.add_car({"type": "Dictionary"})

    print(f"Mixed cargo train: {train}")

    print("\nAccessing different types:")
    for i in range(train.how_many_cars()):
        cargo = train.get_cargo(i)
        print(f"  Car {i}: {cargo} (type: {type(cargo).__name__})")

def test_performance_comparison():
    """Compare some operations with array-like behavior"""
    print("\n=== Performance Comparison Notes ===")
    train = Train()

    # Build a longer train
    print("Building a 10-car train...")
    for i in range(10):
        train.add_car(f"Car-{i}")

    print(f"Final train: {train}")
    print(f"\nKey differences from ArrayList:")
    print("- No capacity/resizing needed")
    print("- O(n) access time (must traverse)")
    print("- O(1) insertion/deletion IF we have the node reference")
    print("- No index shifting needed for insert/remove")
    print("- Memory scattered (not contiguous)")

# Run all tests
if __name__ == "__main__":
    test_basic_operations()
    test_insert_operations()
    test_remove_operations()
    test_edge_cases()
    test_iterator()
    test_mixed_data_types()
    test_performance_comparison()

    print("\n=== All Tests Complete ===")
    print("The train has successfully completed its journey!")
