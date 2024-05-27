import mlflow
from mlflow.tracking import MlflowClient
import click

@click.command()
@click.option(
    "--experiment_name",
    default="random-forest-hyperopt",
)
def restore_experiment(experiment_name):
    client = MlflowClient()

    # Get the experiment by name
    experiment = client.get_experiment_by_name(experiment_name)

    if experiment is None:
        print(f"Experiment '{experiment_name}' does not exist.")
        return

    experiment_id = experiment.experiment_id

    # Restore the experiment
    client.restore_experiment(experiment_id)
    print(f"Experiment '{experiment_name}' with ID '{experiment_id}' has been restored.")


if __name__ == '__main__':
    restore_experiment()