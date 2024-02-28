// tests/tools.test.js

const { v4: uuidv4 } = require("uuid");
const { setupClient } = require("./fixtures"); // Adjust the path as necessary

describe("Tools API", () => {
  let client;

  beforeAll(() => {
    client = setupClient();
  });

  test("tools.get", async () => {
    const agentId = uuidv4();
    const response = await client.tools.get(agentId);
    expect(response.length).toBeGreaterThan(0);
    expect(response[0]).toHaveProperty("type"); // Assuming 'Tool' objects have a 'type' property
  });

  test("tools.create", async () => {
    const response = await client.tools.create({
      agentId: uuidv4(),
      tool: {
        type: "function",
        function: {
          description: "test description",
          name: "test name",
          parameters: { test_arg: "test val" },
        },
      },
    });

    expect(response).toHaveProperty("createdAt");
  });

  test("tools.update", async () => {
    const agentId = uuidv4();
    const toolId = uuidv4();

    const response = await client.tools.update(agentId, toolId, {
      function: {
        description: "test description",
        name: "test name",
        parameters: { test_arg: "test val" },
      },
    });

    expect(response).toHaveProperty("updatedAt");
  });

  test("tools.delete", async () => {
    const response = await client.tools.delete({
      agentId: uuidv4(),
      toolId: uuidv4(),
    });

    expect(response).toBeNull();
  });
});