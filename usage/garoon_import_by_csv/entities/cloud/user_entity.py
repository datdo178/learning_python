import os

file_name = 'import_users_cloud.csv'
output_dir = os.path.dirname(__file__) + '/../../files/' + file_name


class UserCloud:
    def __init__(self):
        self.login_name = ''
        self.display_name = ''
        self.new_login_name = ''
        self.password = ''
        self.surname = ''
        self.given_name = ''
        self.phonetic_surname = ''
        self.phonetic_given_name = ''
        self.localized_name = ''
        self.language_for_localized_name = ''
        self.email_address = ''
        self.status = ''
        self.language = ''
        self.timezone = ''
        self.phone = ''
        self.extension = ''
        self.mobile_phone = ''
        self.url = ''
        self.employee_id = ''
        self.hire_date = ''
        self.birthday = ''
        self.about_me = ''
        self.display_order = ''
        self.skype_name = ''
        self.to_be_deleted = ''

    def create_import_file(self, user_config_data):
        lines = []

        for i in range(1, user_config_data["quantity"] + 1):
            line = []

            self.login_name = f'{user_config_data["loginNamePrefix"]}{i}'
            self.display_name = self.login_name
            self.new_login_name = self.login_name
            self.password = user_config_data['password']
            self.language_for_localized_name = user_config_data['languageForLocalizedName']
            self.status = user_config_data['status']
            self.timezone = user_config_data['timezone']

            line_tmp = vars(self)

            for j in line_tmp:
                line.append(line_tmp[j])

            lines.append('"' + '","'.join(line) + '"')

        output_file = open(output_dir, 'w')
        output_file.write('\n'.join(lines))
        print(f'* [DONE] Created import file - "{file_name}"')
