import { describe, expect, it } from "vitest";
import { userServices } from "./userServices";
import { useRepositoryinMemory } from "../repositories/userRepositoryinMemory";

describe("test user create function", () => {
    it("should crate a user", async() => {
      const user ={
          id: "1",
          name: "Eduardo gonçalves",
          email: "eduardogoncalves8384@gmail.com"
      };
      const userCreated = await userServices.create(user, useRepositoryinMemory);
      expect(userCreated).toHaveProperty("id");
      expect(userCreated).toHaveProperty("name");
    })
})

