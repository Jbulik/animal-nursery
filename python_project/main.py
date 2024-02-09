# меню и запуск

from registry.animal_registry import AnimalRegistry


if __name__ == "__main__":
    registry = AnimalRegistry()

    while True:
        print("\nКонсольное меню:")
        print("1 - Список всех животных")
        print("2 - Завести новое животное")
        print("3 - Вывести список команд животного")
        print("4 - Обучить животное новой команде")
        print("5 - Вывести список животных по дате рождения")
        print("6 - Вывести список животных по группе (Pets/PackAnimals)")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            registry.list_animals_by_birth_date()
        elif choice == '2':
            # Логика добавления новых животных
            pass
        elif choice == '3':
            # Логика вывода списка команд животного
            pass
        elif choice == '4':
            # Логика обучения животного новой команде
            pass
        elif choice == '5':
            # Логика вывода списка животных по дате рождения
            pass
        elif choice == '6':
            group_choice = input("Введите группу животных (Pets/PackAnimals): ")
            registry.list_animals_by_group(group_choice)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
