import { term } from "@pact-foundation/pact/src/dsl/matchers";
import axios from "axios";
import { pactWith } from "jest-pact";
import { fetchBinaryCode } from "./apiClient";

pactWith({ consumer: "frontend", provider: "backend" }, (provider) => {
  beforeEach(() => {
    axios.defaults.baseURL = provider.mockService.baseUrl;
  });

  describe("get EAN8 barcode", () => {
    beforeEach(() => {
      provider.addInteraction({
        state: "",
        uponReceiving: "a request to get an EAN8 barcode",
        withRequest: {
          method: "GET",
          path: "/barcode8/0000000",
          headers: {
            Accept: "application/json",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "image/svg+xml; charset=utf-8" },
          body: term({
            generate: `<?xml version="1.0" encoding="utf-8" ?><svg></svg>`,
            matcher: `^<\\?xml version="1.0" encoding="utf-8" \\?>\\s*<svg.*</svg>$`,
          }),
        },
      });
    });

    it("will receive an EAN8 barcode", async () => {
      const result = await fetchBinaryCode("0000000", "ean8");
      expect(result).toBe(`<?xml version="1.0" encoding="utf-8" ?><svg></svg>`);
    });
  });
});

pactWith({ consumer: "frontend", provider: "backend" }, (provider) => {
  beforeEach(() => {
    axios.defaults.baseURL = provider.mockService.baseUrl;
  });

  describe("get EAN13 barcode", () => {
    beforeEach(() => {
      provider.addInteraction({
        state: "",
        uponReceiving: "a request to get an EAN13 barcode",
        withRequest: {
          method: "GET",
          path: "/barcode13/012345678901",
          headers: {
            Accept: "application/json",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "image/svg+xml; charset=utf-8" },
          body: term({
            generate: `<?xml version="1.0" encoding="utf-8" ?><svg></svg>`,
            matcher: `^<\\?xml version="1.0" encoding="utf-8" \\?>\\s*<svg.*</svg>$`,
          }),
        },
      });
    });

    it("will receive an EAN13 barcode", async () => {
      const result = await fetchBinaryCode("012345678901", "ean13");
      expect(result).toBe(`<?xml version="1.0" encoding="utf-8" ?><svg></svg>`);
    });
  });
});
