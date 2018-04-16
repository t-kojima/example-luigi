import luigi


class Main(luigi.Task):

    def run(self):
        print("hello luigi")


if __name__ == '__main__':
    luigi.build([Main()], local_scheduler=True)
    # luigi.run(main_task_cls=Main, local_scheduler=True)
