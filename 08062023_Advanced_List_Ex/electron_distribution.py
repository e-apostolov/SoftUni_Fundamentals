number_of_electrons = int(input())
shell_distribution = []
shell_position = 0
while number_of_electrons:
    shell_position += 1
    current_shell = 2 * (shell_position ** 2)
    if current_shell <= number_of_electrons:
        number_of_electrons -= current_shell
        shell_distribution.append(current_shell)
    else:
        shell_distribution.append(number_of_electrons)
        break

print(shell_distribution)


