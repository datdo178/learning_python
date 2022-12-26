import os

file_name = 'import_users_onpre.csv'
output_dir = os.path.dirname(__file__) + '/../../files/' + file_name


class UserOnpre:
    def __init__(self):
        self.current_login_name = ''
        self.name = ''
        self.new_login_name = ''
        self.password = ''
        self.locale = ''
        self.office = ''
        self.display_order = ''
        self.status = ''
        self.delete_flag = ''
        self.pronunciation = ''
        self.email = ''
        self.notes = ''
        self.position = ''
        self.contact = ''
        self.url = ''

    def create_import_file(self, user_config_data):

        lines = []

        for i in range(1, user_config_data["quantity"] + 1):
            line = []

            self.current_login_name = f'{user_config_data["loginNamePrefix"]}{i}'
            self.name = self.current_login_name
            self.new_login_name = self.current_login_name
            self.password = user_config_data['password']
            self.status = user_config_data['status']

            line_tmp = vars(self)

            for j in line_tmp:
                line.append(line_tmp[j])

            lines.append('"' + '","'.join(line) + '"')

        output_file = open(output_dir, 'w')
        output_file.write('\n'.join(lines))
        print(f'* [DONE] Created import file - "{file_name}"')
