# Tests for agent queries
from pycozo import Client
from uuid import uuid4
from ward import test

from .create_agent import create_agent_query
from .delete_agent import delete_agent_query
from .get_agent import get_agent_query
from .list_agents import list_agents_query
from .update_agent import update_agent_query
from .schema import init


def cozo_client():
    # Create a new client for each test
    # and initialize the schema.
    client = Client()

    init(client)

    return client


@test("create agent")
def _():
    client = cozo_client()
    agent_id = uuid4()

    query = create_agent_query(
        agent_id=agent_id,
        name="test agent",
        about="test agent about",
    )

    client.run(query)


@test("get agent not exists")
def _():
    client = cozo_client()
    agent_id = uuid4()

    query = get_agent_query(
        agent_id=agent_id,
    )

    result = client.run(query)

    assert len(result["agent_id"]) == 0


@test("get agent exists")
def _():
    client = cozo_client()
    agent_id = uuid4()

    query = create_agent_query(
        agent_id=agent_id,
        name="test agent",
        about="test agent about",
        default_settings={"temperature": 1.5},
    )

    client.run(query)

    query = get_agent_query(
        agent_id=agent_id,
    )

    result = client.run(query)

    assert len(result["agent_id"]) == 1
    assert "temperature" in result["default_settings"][0]
    assert result["default_settings"][0]["temperature"] == 1.5


@test("delete agent")
def _():
    client = cozo_client()
    agent_id = uuid4()

    # Create the agent
    query = create_agent_query(
        agent_id=agent_id,
        name="test agent",
        about="test agent about",
    )

    client.run(query)

    # Delete the agent
    query = delete_agent_query(
        agent_id=agent_id,
    )

    client.run(query)

    # Check that the agent is deleted
    query = get_agent_query(
        agent_id=agent_id,
    )

    result = client.run(query)

    assert len(result["agent_id"]) == 0


@test("update agent")
def _():
    client = cozo_client()
    agent_id = uuid4()

    create_query = create_agent_query(
        agent_id=agent_id,
        name="test agent",
        about="test agent about",
    )

    client.run(create_query)

    update_query = update_agent_query(
        agent_id=agent_id,
        name="updated agent",
        about="updated agent about",
        default_settings={"temperature": 1.5},
    )

    result = client.run(update_query)
    data = result.iloc[0].to_dict()

    assert data["updated_at"] > data["created_at"]


@test("list agents")
def _():
    client = cozo_client()

    query = list_agents_query()

    result = client.run(query)

    assert len(result["agent_id"]) == 0