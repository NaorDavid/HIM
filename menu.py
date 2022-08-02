from simple_term_menu import TerminalMenu

main_menu_options = ["[x] option # 1","[a] option # 2","[b] option # 3","[c] option # 4","[d] option # 5",
                     "[e] option # 6","[f] option # 7","[g] option # 8","[q] quit"]

main_menu = TerminalMenu(main_menu_options)

quit_flag = True
while quit_flag:
    main_menu_options_index = main_menu.show()
    main_menu_option_choice = main_menu_options[main_menu_options_index]
    if(main_menu_option_choice == "[q] quit"):
        quit_flag = False
    