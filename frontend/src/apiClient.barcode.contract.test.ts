import { term } from "@pact-foundation/pact/src/dsl/matchers";
import axios from "axios";
import { pactWith } from "jest-pact";
import { fetchBarCode } from "./apiClient";

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
          method: "POST",
          path: "/barcode/ean8",
          body: "0000000",
          headers: {
            Accept: "image/svg+xml",
            "Content-Type": "text/plain",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "image/svg+xml; charset=utf-8" },
          body: term({
            generate: `<svg></svg>`,
            matcher: `<svg.*</svg>$`,
          }),
        },
      });
    });

    it("will receive an EAN8 barcode", async () => {
      const result = await fetchBarCode("0000000", "ean8");
      expect(result).toBe(`<svg></svg>`);
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
          method: "POST",
          path: "/barcode/ean13",
          body: "012345678901",
          headers: {
            Accept: "image/svg+xml",
            "Content-Type": "text/plain",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "image/svg+xml; charset=utf-8" },
          body: term({
            generate: `<svg></svg>`,
            matcher: `<svg.*</svg>$`,
          }),
        },
      });
    });

    it("will receive an EAN13 barcode", async () => {
      const result = await fetchBarCode("012345678901", "ean13");
      expect(result).toBe(`<svg></svg>`);
    });
  });
});

pactWith({ consumer: "frontend", provider: "backend" }, (provider) => {
  beforeEach(() => {
    axios.defaults.baseURL = provider.mockService.baseUrl;
  });

  describe("get CODE39 barcode", () => {
    beforeEach(() => {
      provider.addInteraction({
        state: "",
        uponReceiving: "a request to get an CODE39 barcode",
        withRequest: {
          method: "POST",
          path: "/barcode/code39",
          body: "ABCDEFGHIJKLMNOPQRSTUVWXZ01234567890$./ -%+",
          headers: {
            Accept: "image/svg+xml",
            "Content-Type": "text/plain",
          },
        },
        willRespondWith: {
          status: 200,
          headers: { "Content-Type": "image/svg+xml; charset=utf-8" },
          body: term({
            generate: `<svg></svg>`,
            matcher: `<svg.*</svg>$`,
          }),
        },
      });
    });

    it("will receive an CODE39 barcode", async () => {
      const result = await fetchBarCode(
        "ABCDEFGHIJKLMNOPQRSTUVWXZ01234567890$./ -%+",
        "code39"
      );
      expect(result).toBe(`<svg></svg>`);
    });
  });
});
