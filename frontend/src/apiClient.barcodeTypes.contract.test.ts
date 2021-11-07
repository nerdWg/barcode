import { like, term } from "@pact-foundation/pact/src/dsl/matchers";
import axios from "axios";
import { pactWith } from "jest-pact";
import { fetchBarCodeList } from "./apiClient";

pactWith({ consumer: "frontend", provider: "backend" }, (provider) => {
  beforeEach(() => {
    axios.defaults.baseURL = provider.mockService.baseUrl;
  });

  describe("get available barcode types", () => {
    beforeEach(() => {
      provider.addInteraction({
        state: "",
        uponReceiving: "a request to get available barcode types",
        withRequest: {
          method: "GET",
          path: "/barcodes",
          headers: {
            Accept: "application/json",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "application/json" },
          body: like(["ean8", "ean13", "code39", "code128"]),
        },
      });
    });

    it("will receive a list of available barcode types", async () => {
      const result = await fetchBarCodeList();
      expect(result).toEqual(["ean8", "ean13", "code39", "code128"]);
    });
  });
});
