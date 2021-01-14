import React, { useState } from "react";

export default function CheckBox(props) {
  console.log(props.days);
  function onChange(e) {
    e.preventDefault();
  }
  return (
    <React.Fragment>
      <div className="mx-3">
        <p className="mt-3">days</p>
        <div className="form-check form-check-inline">
          <input
            class="form-check-input"
            type="radio"
            name="inlineRadioOptions"
            id="inlineRadio1"
            value="14"
            onChange={(e) => {
              props.setDays(e.target.value);
            }}
          />
          <label class="form-check-label" for="inlineRadio1">
            14
          </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="radio"
            name="inlineRadioOptions"
            id="inlineRadio2"
            value="20"
            onChange={(e) => {
              props.setDays(e.target.value);
            }}
          />
          <label class="form-check-label" for="inlineRadio2">
            20
          </label>
        </div>
        <form
          onSubmit={(e) => {
            e.preventDefault()
            props.makeReq();
          }}
        >
          <div className="row">
            <div class="form-group col-4">
              <label for="formGroupExampleInput">ratio</label>
              <input
                type="text"
                class="form-control"
                id="formGroupExampleInput"
                placeholder="default ratio .6"
                onChange={(e) => {
                  props.setGoldenRatio(e.target.value);
                }}
              />
            </div>
            <div class="form-group col-4">
              <label for="formGroupExampleInput2">volume</label>
              <input
                type="text"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="default volume 500 "
                onChange={(e) => {
                  props.setVolume(e.target.value);
                }}
              />
            </div>
            <div class="form-group col-4">
              <label for="formGroupExampleInput2">open interest</label>
              <input
                type="text"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="default oi 1000"
                onChange={(e) => {
                  props.setOi(e.target.value);
                }}
              />
            </div>
          </div>
          <button
            type="submit"
            class="btn btn-primary"
            onSubmit={(e) => {
              e.preventDefault()
              props.makeReq();
            }}
          >
            Submit
          </button>
        </form>
      </div>
    </React.Fragment>
  );
}
