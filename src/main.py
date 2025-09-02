class Run:
    @staticmethod
    def run_main() -> None:
        pass

    @staticmethod
    def run_testing_file(filename:str) -> None:
        import subprocess
        import os

        filename = os.path.realpath(f'testing_pygame/{filename}.py')

        if os.path.exists(filename):
            result = subprocess.run(['python', f'{str(filename)}'], capture_output=True, text=True,shell=True)
            print(f'Stdout: {result.stdout}')
            print(f'Errors: {result.stderr}')
        else:
            print(f'The file "{filename}" not exists!')