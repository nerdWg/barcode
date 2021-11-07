import { like, term } from "@pact-foundation/pact/src/dsl/matchers";
import axios from "axios";
import { pactWith } from "jest-pact";
import { fetchBinaryCode } from "./apiClient";

pactWith({ consumer: "frontend", provider: "backend" }, (provider) => {
  beforeEach(() => {
    axios.defaults.baseURL = provider.mockService.baseUrl;
  });

  describe("get binary ean8 code", () => {
    beforeEach(() => {
      provider.addInteraction({
        state: "",
        uponReceiving: "a request to get an EAN8 binary code",
        withRequest: {
          method: "POST",
          path: "/barcode/ean8",
          headers: {
            Accept: "text/plain",
            "Content-Type": "text/plain",
          },
          body: "0000000",
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "text/plain; charset=utf-8" },
          body: term({
            generate:
              "101 0001101 0001101 0001101 0001101 0001101 0001101 01010 1110010 1110010 1110010 1110010 1110010 1110010 101",
            matcher: "^[01 ]+$",
          }),
        },
      });
    });

    it("will receive an EAN8 binary code", async () => {
      const result = await fetchBinaryCode("0000000", "ean8");
      expect(result).toBe(
        "101 0001101 0001101 0001101 0001101 0001101 0001101 01010 1110010 1110010 1110010 1110010 1110010 1110010 101"
      );
    });
  });
});
pactWith({ consumer: "frontend", provider: "backend" }, (provider) => {
  beforeEach(() => {
    axios.defaults.baseURL = provider.mockService.baseUrl;
  });

  describe("get binary ean13 code", () => {
    beforeEach(() => {
      provider.addInteraction({
        state: "",
        uponReceiving: "a request to get an EAN13 binary code",
        withRequest: {
          method: "POST",
          path: "/barcode/ean13",
          body: "012345678901",
          headers: {
            Accept: "text/plain",
            "Content-Type": "text/plain",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "text/plain; charset=utf-8" },
          body: like(
            "101 0001101 0001101 0001101 0001101 0001101 0001101 01010 1110010 1110010 1110010 1110010 1110010 1110010 101"
          ),
        },
      });
    });

    it("will receive an EAN13 binary code", async () => {
      const result = await fetchBinaryCode("012345678901", "ean13");
      expect(result).toBe(
        "101 0001101 0001101 0001101 0001101 0001101 0001101 01010 1110010 1110010 1110010 1110010 1110010 1110010 101"
      );
    });
  });
});
