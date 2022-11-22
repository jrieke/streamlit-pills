import { Streamlit, RenderData } from "streamlit-component-lib"

const labelDiv = document.body.appendChild(document.createElement("label"))
const label = labelDiv.appendChild(document.createTextNode(""))
const container = document.body.appendChild(document.createElement("div"))
container.classList.add("container")

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event: Event): void {
  // Get the RenderData from the event
  const data = (event as CustomEvent<RenderData>).detail

  label.textContent = data.args["label"]
  let options = data.args["options"]
  let icons = data.args["icons"]
  let index = data.args["index"]
  let clearable = data.args["clearable"]
  // console.log(captions)

  if (container.childNodes.length === 0) {
    options.forEach((option: string, i: number) => {
      let pill = container.appendChild(document.createElement("div"))
      pill.classList.add("pill")

      if (icons) {
        let icon_span = pill.appendChild(document.createElement("span"))
        icon_span.classList.add("icon")
        icon_span.textContent = icons[i]
      }

      pill.appendChild(document.createTextNode(option))

      if (i === index) {
        pill.classList.add("selected")
      }

      pill.onclick = function () {
        // If the element is clearable, let the user unselect by clicking on the pill
        // again. I.e. if this pill (which is clicked) was already selected before, we
        // unselect it later.
        let unselect = clearable && pill.classList.contains("selected")

        container.querySelectorAll(".selected").forEach((el) => {
          el.classList.remove("selected")
        })

        if (unselect) {
          // Need to pass a string here and convert it to None on the Python side.
          // If setting null, the components lib returns the "default" value (=index).
          Streamlit.setComponentValue("None")
        } else {
          Streamlit.setComponentValue(i)
          pill.classList.add("selected")
        }
      }
    })
  }

  // Style according to the app theme.
  if (data.theme) {
    labelDiv.style.font = data.theme.font
    labelDiv.style.color = data.theme.textColor
    // TODO: Update this with correct classes.
    if (data.theme.base === "dark") {
      document.body.querySelectorAll(".pill").forEach((el) => {
        el.classList.add("dark")
      })
    } else {
      document.body.querySelectorAll(".pill").forEach((el) => {
        el.classList.remove("dark")
      })
    }

    // TODO: Gray out the component and disable click if it's disabled.
  }

  // We tell Streamlit to update our frameHeight after each render event, in
  // case it has changed. (This isn't strictly necessary for the example
  // because our height stays fixed, but this is a low-cost function, so
  // there's no harm in doing it redundantly.)
  Streamlit.setFrameHeight()
}

// Attach our `onRender` handler to Streamlit's render event.
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

// Tell Streamlit we're ready to start receiving data. We won't get our
// first RENDER_EVENT until we call this function.
Streamlit.setComponentReady()

// Finally, tell Streamlit to update our initial height. We omit the
// `height` parameter here to have it default to our scrollHeight.
Streamlit.setFrameHeight()
