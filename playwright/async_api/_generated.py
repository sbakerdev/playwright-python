# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pathlib
import sys
import typing

if sys.version_info >= (3, 8):  # pragma: no cover
    from typing import Literal
else:  # pragma: no cover
    from typing_extensions import Literal

from playwright._impl._accessibility import Accessibility as AccessibilityImpl
from playwright._impl._api_structures import (
    Cookie,
    FilePayload,
    FloatRect,
    Geolocation,
    HttpCredentials,
    PdfMargins,
    Position,
    ProxySettings,
    ResourceTiming,
    SourceLocation,
    StorageState,
    ViewportSize,
)
from playwright._impl._async_base import AsyncBase, AsyncEventContextManager, mapping
from playwright._impl._browser import Browser as BrowserImpl
from playwright._impl._browser_context import BrowserContext as BrowserContextImpl
from playwright._impl._browser_type import BrowserType as BrowserTypeImpl
from playwright._impl._cdp_session import CDPSession as CDPSessionImpl
from playwright._impl._chromium_browser_context import (
    ChromiumBrowserContext as ChromiumBrowserContextImpl,
)
from playwright._impl._console_message import ConsoleMessage as ConsoleMessageImpl
from playwright._impl._dialog import Dialog as DialogImpl
from playwright._impl._download import Download as DownloadImpl
from playwright._impl._element_handle import ElementHandle as ElementHandleImpl
from playwright._impl._file_chooser import FileChooser as FileChooserImpl
from playwright._impl._frame import Frame as FrameImpl
from playwright._impl._input import Keyboard as KeyboardImpl
from playwright._impl._input import Mouse as MouseImpl
from playwright._impl._input import Touchscreen as TouchscreenImpl
from playwright._impl._js_handle import JSHandle as JSHandleImpl
from playwright._impl._network import Request as RequestImpl
from playwright._impl._network import Response as ResponseImpl
from playwright._impl._network import Route as RouteImpl
from playwright._impl._network import WebSocket as WebSocketImpl
from playwright._impl._page import Page as PageImpl
from playwright._impl._page import Worker as WorkerImpl
from playwright._impl._playwright import Playwright as PlaywrightImpl
from playwright._impl._selectors import Selectors as SelectorsImpl
from playwright._impl._video import Video as VideoImpl

NoneType = type(None)


class Request(AsyncBase):
    def __init__(self, obj: RequestImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Request.url

        URL of the request.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def resource_type(self) -> str:
        """Request.resource_type

        Contains the request's resource type as it was perceived by the rendering engine. ResourceType will be one of the
        following: `document`, `stylesheet`, `image`, `media`, `font`, `script`, `texttrack`, `xhr`, `fetch`, `eventsource`,
        `websocket`, `manifest`, `other`.

        > NOTE: The resource types are available as constants in [ResourceTypes].

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.resource_type)

    @property
    def method(self) -> str:
        """Request.method

        Request's method (GET, POST, etc.)

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.method)

    @property
    def post_data(self) -> typing.Optional[str]:
        """Request.post_data

        Request's post body, if any.

        Returns
        -------
        Union[str, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.post_data)

    @property
    def post_data_json(self) -> typing.Optional[typing.Any]:
        """Request.post_data_json

        Returns parsed request's body for `form-urlencoded` and JSON as a fallback if any.

        When the response is `application/x-www-form-urlencoded` then a key/value object of the values will be returned.
        Otherwise it will be parsed as JSON.

        Returns
        -------
        Union[Any, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.post_data_json)

    @property
    def post_data_buffer(self) -> typing.Optional[bytes]:
        """Request.post_data_buffer

        Request's post body in a binary form, if any.

        Returns
        -------
        Union[bytes, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.post_data_buffer)

    @property
    def headers(self) -> typing.Dict[str, str]:
        """Request.headers

        An object with HTTP headers associated with the request. All header names are lower-case.

        Returns
        -------
        Dict[str, str]
        """
        return mapping.from_maybe_impl(self._impl_obj.headers)

    @property
    def frame(self) -> "Frame":
        """Request.frame

        Returns the `Frame` that initiated this request.

        Returns
        -------
        Frame
        """
        return mapping.from_impl(self._impl_obj.frame)

    @property
    def redirected_from(self) -> typing.Optional["Request"]:
        """Request.redirected_from

        Request that was redirected by the server to this one, if any.

        When the server responds with a redirect, Playwright creates a new `Request` object. The two requests are connected by
        `redirectedFrom()` and `redirectedTo()` methods. When multiple server redirects has happened, it is possible to
        construct the whole redirect chain by repeatedly calling `redirectedFrom()`.

        For example, if the website `http://example.com` redirects to `https://example.com`:

        ```py
        response = await page.goto(\"http://example.com\")
        print(response.request.redirected_from.url) # \"http://example.com\"
        ```

        If the website `https://google.com` has no redirects:

        ```py
        response = await page.goto(\"https://google.com\")
        print(response.request.redirected_from) # None
        ```

        Returns
        -------
        Union[Request, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.redirected_from)

    @property
    def redirected_to(self) -> typing.Optional["Request"]:
        """Request.redirected_to

        New request issued by the browser if the server responded with redirect.

        This method is the opposite of `request.redirected_from()`:

        ```py
        assert request.redirected_from.redirected_to == request
        ```

        Returns
        -------
        Union[Request, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.redirected_to)

    @property
    def failure(self) -> typing.Optional[str]:
        """Request.failure

        The method returns `null` unless this request has failed, as reported by `requestfailed` event.

        Example of logging of all the failed requests:

        ```py
        page.on(\"requestfailed\", lambda request: print(request.url + \" \" + request.failure))
        ```

        Returns
        -------
        Union[str, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.failure)

    @property
    def timing(self) -> ResourceTiming:
        """Request.timing

        Returns resource timing information for given request. Most of the timing values become available upon the response,
        `responseEnd` becomes available when request finishes. Find more information at
        [Resource Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming).

        ```py
        async with page.expect_event(\"requestfinished\") as request_info:
            await page.goto(\"http://example.com\")
        request = await request_info.value
        print(request.timing)
        ```

        Returns
        -------
        {startTime: float, domainLookupStart: float, domainLookupEnd: float, connectStart: float, secureConnectionStart: float, connectEnd: float, requestStart: float, responseStart: float, responseEnd: float}
        """
        return mapping.from_impl(self._impl_obj.timing)

    async def response(self) -> typing.Optional["Response"]:
        """Request.response

        Returns the matching `Response` object, or `null` if the response was not received due to error.

        Returns
        -------
        Union[Response, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async("request.response", self._impl_obj.response())
        )

    def is_navigation_request(self) -> bool:
        """Request.is_navigation_request

        Whether this request is driving frame's navigation.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(self._impl_obj.is_navigation_request())


mapping.register(RequestImpl, Request)


class Response(AsyncBase):
    def __init__(self, obj: ResponseImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Response.url

        Contains the URL of the response.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def ok(self) -> bool:
        """Response.ok

        Contains a boolean stating whether the response was successful (status in the range 200-299) or not.

        Returns
        -------
        bool
        """
        return mapping.from_maybe_impl(self._impl_obj.ok)

    @property
    def status(self) -> int:
        """Response.status

        Contains the status code of the response (e.g., 200 for a success).

        Returns
        -------
        int
        """
        return mapping.from_maybe_impl(self._impl_obj.status)

    @property
    def status_text(self) -> str:
        """Response.status_text

        Contains the status text of the response (e.g. usually an \"OK\" for a success).

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.status_text)

    @property
    def headers(self) -> typing.Dict[str, str]:
        """Response.headers

        Returns the object with HTTP headers associated with the response. All header names are lower-case.

        Returns
        -------
        Dict[str, str]
        """
        return mapping.from_maybe_impl(self._impl_obj.headers)

    @property
    def request(self) -> "Request":
        """Response.request

        Returns the matching `Request` object.

        Returns
        -------
        Request
        """
        return mapping.from_impl(self._impl_obj.request)

    @property
    def frame(self) -> "Frame":
        """Response.frame

        Returns the `Frame` that initiated this response.

        Returns
        -------
        Frame
        """
        return mapping.from_impl(self._impl_obj.frame)

    async def finished(self) -> typing.Optional[str]:
        """Response.finished

        Waits for this response to finish, returns failure error if request failed.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async("response.finished", self._impl_obj.finished())
        )

    async def body(self) -> bytes:
        """Response.body

        Returns the buffer with response body.

        Returns
        -------
        bytes
        """

        return mapping.from_maybe_impl(
            await self._async("response.body", self._impl_obj.body())
        )

    async def text(self) -> str:
        """Response.text

        Returns the text representation of response body.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("response.text", self._impl_obj.text())
        )

    async def json(self) -> typing.Any:
        """Response.json

        Returns the JSON representation of response body.

        This method will throw if the response body is not parsable via `JSON.parse`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async("response.json", self._impl_obj.json())
        )


mapping.register(ResponseImpl, Response)


class Route(AsyncBase):
    def __init__(self, obj: RouteImpl):
        super().__init__(obj)

    @property
    def request(self) -> "Request":
        """Route.request

        A request to be routed.

        Returns
        -------
        Request
        """
        return mapping.from_impl(self._impl_obj.request)

    async def abort(self, error_code: str = None) -> NoneType:
        """Route.abort

        Aborts the route's request.

        Parameters
        ----------
        error_code : Union[str, NoneType]
            Optional error code. Defaults to `failed`, could be one of the following:
            - `'aborted'` - An operation was aborted (due to user action)
            - `'accessdenied'` - Permission to access a resource, other than the network, was denied
            - `'addressunreachable'` - The IP address is unreachable. This usually means that there is no route to the specified
              host or network.
            - `'blockedbyclient'` - The client chose to block the request.
            - `'blockedbyresponse'` - The request failed because the response was delivered along with requirements which are not
              met ('X-Frame-Options' and 'Content-Security-Policy' ancestor checks, for instance).
            - `'connectionaborted'` - A connection timed out as a result of not receiving an ACK for data sent.
            - `'connectionclosed'` - A connection was closed (corresponding to a TCP FIN).
            - `'connectionfailed'` - A connection attempt failed.
            - `'connectionrefused'` - A connection attempt was refused.
            - `'connectionreset'` - A connection was reset (corresponding to a TCP RST).
            - `'internetdisconnected'` - The Internet connection has been lost.
            - `'namenotresolved'` - The host name could not be resolved.
            - `'timedout'` - An operation timed out.
            - `'failed'` - A generic failure occurred.
        """

        return mapping.from_maybe_impl(
            await self._async("route.abort", self._impl_obj.abort(errorCode=error_code))
        )

    async def fulfill(
        self,
        *,
        status: int = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        body: typing.Union[str, bytes] = None,
        path: typing.Union[str, pathlib.Path] = None,
        content_type: str = None
    ) -> NoneType:
        """Route.fulfill

        Fulfills route's request with given response.

        An example of fulfilling all requests with 404 responses:

        ```py
        await page.route(\"**/*\", lambda route: route.fulfill(
            status=404,
            content_type=\"text/plain\",
            body=\"not found!\"))
        ```

        An example of serving static file:

        ```py
        await page.route(\"**/xhr_endpoint\", lambda route: route.fulfill(path=\"mock_data.json\"))
        ```

        Parameters
        ----------
        status : Union[int, NoneType]
            Response status code, defaults to `200`.
        headers : Union[Dict[str, str], NoneType]
            Response headers. Header values will be converted to a string.
        body : Union[bytes, str, NoneType]
            Response body.
        path : Union[pathlib.Path, str, NoneType]
            File path to respond with. The content type will be inferred from file extension. If `path` is a relative path, then it
            is resolved relative to the current working directory.
        content_type : Union[str, NoneType]
            If set, equals to setting `Content-Type` response header.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "route.fulfill",
                self._impl_obj.fulfill(
                    status=status,
                    headers=mapping.to_impl(headers),
                    body=body,
                    path=path,
                    contentType=content_type,
                ),
            )
        )

    async def continue_(
        self,
        *,
        url: str = None,
        method: str = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        post_data: typing.Union[str, bytes] = None
    ) -> NoneType:
        """Route.continue_

        Continues route's request with optional overrides.

        ```py
        async def handle(route, request):
            # override headers
            headers = {
                **request.headers,
                \"foo\": \"bar\" # set \"foo\" header
                \"origin\": None # remove \"origin\" header
            }
            await route.continue(headers=headers)
        }
        await page.route(\"**/*\", handle)
        ```

        Parameters
        ----------
        url : Union[str, NoneType]
            If set changes the request URL. New URL must have same protocol as original one.
        method : Union[str, NoneType]
            If set changes the request method (e.g. GET or POST)
        headers : Union[Dict[str, str], NoneType]
            If set changes the request HTTP headers. Header values will be converted to a string.
        post_data : Union[bytes, str, NoneType]
            If set changes the post data of request
        """

        return mapping.from_maybe_impl(
            await self._async(
                "route.continue_",
                self._impl_obj.continue_(
                    url=url,
                    method=method,
                    headers=mapping.to_impl(headers),
                    postData=post_data,
                ),
            )
        )


mapping.register(RouteImpl, Route)


class WebSocket(AsyncBase):
    def __init__(self, obj: WebSocketImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """WebSocket.url

        Contains the URL of the WebSocket.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    def expect_event(
        self, event: str, predicate: typing.Callable = None, *, timeout: float = None
    ) -> AsyncEventContextManager:
        """WebSocket.expect_event

        Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
        value. Will throw an error if the webSocket is closed before the event is fired. Returns the event data value.

        Parameters
        ----------
        event : str
            Event name, same one would pass into `webSocket.on(event)`.
        predicate : Union[Callable, NoneType]
            Receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_event(
                event=event, predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    async def wait_for_event(
        self, event: str, predicate: typing.Callable = None, *, timeout: float = None
    ) -> typing.Any:
        """WebSocket.wait_for_event

        > NOTE: In most cases, you should use `web_socket.expect_event()`.

        Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function and
        waits for `predicate(event)` to return a truthy value. Will throw an error if the socket is closed before the `event` is
        fired.

        Parameters
        ----------
        event : str
            Event name, same one typically passed into `*.on(event)`.
        predicate : Union[Callable, NoneType]
            Receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "web_socket.wait_for_event",
                self._impl_obj.wait_for_event(
                    event=event,
                    predicate=self._wrap_handler(predicate),
                    timeout=timeout,
                ),
            )
        )

    def is_closed(self) -> bool:
        """WebSocket.is_closed

        Indicates that the web socket has been closed.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(self._impl_obj.is_closed())


mapping.register(WebSocketImpl, WebSocket)


class Keyboard(AsyncBase):
    def __init__(self, obj: KeyboardImpl):
        super().__init__(obj)

    async def down(self, key: str) -> NoneType:
        """Keyboard.down

        Dispatches a `keydown` event.

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        If `key` is a modifier key, `Shift`, `Meta`, `Control`, or `Alt`, subsequent key presses will be sent with that modifier
        active. To release the modifier key, use `keyboard.up()`.

        After the key is pressed once, subsequent calls to `keyboard.down()` will have
        [repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat) set to true. To release the key, use
        `keyboard.up()`.

        > NOTE: Modifier keys DO influence `keyboard.down`. Holding down `Shift` will type the text in upper case.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        """

        return mapping.from_maybe_impl(
            await self._async("keyboard.down", self._impl_obj.down(key=key))
        )

    async def up(self, key: str) -> NoneType:
        """Keyboard.up

        Dispatches a `keyup` event.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        """

        return mapping.from_maybe_impl(
            await self._async("keyboard.up", self._impl_obj.up(key=key))
        )

    async def insert_text(self, text: str) -> NoneType:
        """Keyboard.insert_text

        Dispatches only `input` event, does not emit the `keydown`, `keyup` or `keypress` events.

        ```py
        await page.keyboard.insert_text(\"嗨\")
        ```

        > NOTE: Modifier keys DO NOT effect `keyboard.insertText`. Holding down `Shift` will not type the text in upper case.

        Parameters
        ----------
        text : str
            Sets input to the specified text value.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "keyboard.insert_text", self._impl_obj.insert_text(text=text)
            )
        )

    async def type(self, text: str, *, delay: float = None) -> NoneType:
        """Keyboard.type

        Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

        To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

        ```py
        await page.keyboard.type(\"Hello\") # types instantly
        await page.keyboard.type(\"World\", delay=100) # types slower, like a user
        ```

        > NOTE: Modifier keys DO NOT effect `keyboard.type`. Holding down `Shift` will not type the text in upper case.

        Parameters
        ----------
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "keyboard.type", self._impl_obj.type(text=text, delay=delay)
            )
        )

    async def press(self, key: str, *, delay: float = None) -> NoneType:
        """Keyboard.press

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: \"Control+o\"` or `key: \"Control+Shift+T\"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        ```py
        page = await browser.new_page()
        await page.goto(\"https://keycode.info\")
        await page.keyboard.press(\"a\")
        await page.screenshot(path=\"a.png\")
        await page.keyboard.press(\"ArrowLeft\")
        await page.screenshot(path=\"arrow_left.png\")
        await page.keyboard.press(\"Shift+O\")
        await page.screenshot(path=\"o.png\")
        await browser.close()
        ```

        Shortcut for `keyboard.down()` and `keyboard.up()`.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "keyboard.press", self._impl_obj.press(key=key, delay=delay)
            )
        )


mapping.register(KeyboardImpl, Keyboard)


class Mouse(AsyncBase):
    def __init__(self, obj: MouseImpl):
        super().__init__(obj)

    async def move(self, x: float, y: float, *, steps: int = None) -> NoneType:
        """Mouse.move

        Dispatches a `mousemove` event.

        Parameters
        ----------
        x : float
        y : float
        steps : Union[int, NoneType]
            defaults to 1. Sends intermediate `mousemove` events.
        """

        return mapping.from_maybe_impl(
            await self._async("mouse.move", self._impl_obj.move(x=x, y=y, steps=steps))
        )

    async def down(
        self,
        *,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None
    ) -> NoneType:
        """Mouse.down

        Dispatches a `mousedown` event.

        Parameters
        ----------
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        """

        return mapping.from_maybe_impl(
            await self._async(
                "mouse.down", self._impl_obj.down(button=button, clickCount=click_count)
            )
        )

    async def up(
        self,
        *,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None
    ) -> NoneType:
        """Mouse.up

        Dispatches a `mouseup` event.

        Parameters
        ----------
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        """

        return mapping.from_maybe_impl(
            await self._async(
                "mouse.up", self._impl_obj.up(button=button, clickCount=click_count)
            )
        )

    async def click(
        self,
        x: float,
        y: float,
        *,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None
    ) -> NoneType:
        """Mouse.click

        Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`.

        Parameters
        ----------
        x : float
        y : float
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        """

        return mapping.from_maybe_impl(
            await self._async(
                "mouse.click",
                self._impl_obj.click(
                    x=x, y=y, delay=delay, button=button, clickCount=click_count
                ),
            )
        )

    async def dblclick(
        self,
        x: float,
        y: float,
        *,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None
    ) -> NoneType:
        """Mouse.dblclick

        Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`, `mouse.down()` and
        `mouse.up()`.

        Parameters
        ----------
        x : float
        y : float
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "mouse.dblclick",
                self._impl_obj.dblclick(x=x, y=y, delay=delay, button=button),
            )
        )


mapping.register(MouseImpl, Mouse)


class Touchscreen(AsyncBase):
    def __init__(self, obj: TouchscreenImpl):
        super().__init__(obj)

    async def tap(self, x: float, y: float) -> NoneType:
        """Touchscreen.tap

        Dispatches a `touchstart` and `touchend` event with a single touch at the position (`x`,`y`).

        Parameters
        ----------
        x : float
        y : float
        """

        return mapping.from_maybe_impl(
            await self._async("touchscreen.tap", self._impl_obj.tap(x=x, y=y))
        )


mapping.register(TouchscreenImpl, Touchscreen)


class JSHandle(AsyncBase):
    def __init__(self, obj: JSHandleImpl):
        super().__init__(obj)

    async def evaluate(self, expression: str, arg: typing.Any = None) -> typing.Any:
        """JSHandle.evaluate

        Returns the return value of `expression`.

        This method passes this handle as the first argument to `expression`.

        If `expression` returns a [Promise], then `handle.evaluate` would wait for the promise to resolve and return its value.

        Examples:

        ```py
        tweet_handle = await page.query_selector(\".tweet .retweets\")
        assert await tweet_handle.evaluate(\"node => node.innerText\") == \"10 retweets\"
        ```

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "js_handle.evaluate",
                self._impl_obj.evaluate(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def evaluate_handle(
        self, expression: str, arg: typing.Any = None
    ) -> "JSHandle":
        """JSHandle.evaluate_handle

        Returns the return value of `expression` as a `JSHandle`.

        This method passes this handle as the first argument to `expression`.

        The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle` returns
        `JSHandle`.

        If the function passed to the `jsHandle.evaluateHandle` returns a [Promise], then `jsHandle.evaluateHandle` would wait
        for the promise to resolve and return its value.

        See `page.evaluate_handle()` for more details.

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "js_handle.evaluate_handle",
                self._impl_obj.evaluate_handle(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def get_property(self, property_name: str) -> "JSHandle":
        """JSHandle.get_property

        Fetches a single property from the referenced object.

        Parameters
        ----------
        property_name : str
            property to get

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "js_handle.get_property",
                self._impl_obj.get_property(propertyName=property_name),
            )
        )

    async def get_properties(self) -> typing.Dict[str, "JSHandle"]:
        """JSHandle.get_properties

        The method returns a map with **own property names** as keys and JSHandle instances for the property values.

        ```py
        handle = await page.evaluate_handle(\"{window, document}\")
        properties = await handle.get_properties()
        window_handle = properties.get(\"window\")
        document_handle = properties.get(\"document\")
        await handle.dispose()
        ```

        Returns
        -------
        Dict[str, JSHandle]
        """

        return mapping.from_impl_dict(
            await self._async(
                "js_handle.get_properties", self._impl_obj.get_properties()
            )
        )

    def as_element(self) -> typing.Optional["ElementHandle"]:
        """JSHandle.as_element

        Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(self._impl_obj.as_element())

    async def dispose(self) -> NoneType:
        """JSHandle.dispose

        The `jsHandle.dispose` method stops referencing the element handle.
        """

        return mapping.from_maybe_impl(
            await self._async("js_handle.dispose", self._impl_obj.dispose())
        )

    async def json_value(self) -> typing.Any:
        """JSHandle.json_value

        Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

        > NOTE: The method will return an empty JSON object if the referenced object is not stringifiable. It will throw an
        error if the object has circular references.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async("js_handle.json_value", self._impl_obj.json_value())
        )


mapping.register(JSHandleImpl, JSHandle)


class ElementHandle(JSHandle):
    def __init__(self, obj: ElementHandleImpl):
        super().__init__(obj)

    def as_element(self) -> typing.Optional["ElementHandle"]:
        """ElementHandle.as_element

        Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(self._impl_obj.as_element())

    async def owner_frame(self) -> typing.Optional["Frame"]:
        """ElementHandle.owner_frame

        Returns the frame containing the given element.

        Returns
        -------
        Union[Frame, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "element_handle.owner_frame", self._impl_obj.owner_frame()
            )
        )

    async def content_frame(self) -> typing.Optional["Frame"]:
        """ElementHandle.content_frame

        Returns the content frame for element handles referencing iframe nodes, or `null` otherwise

        Returns
        -------
        Union[Frame, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "element_handle.content_frame", self._impl_obj.content_frame()
            )
        )

    async def get_attribute(self, name: str) -> typing.Optional[str]:
        """ElementHandle.get_attribute

        Returns element attribute value.

        Parameters
        ----------
        name : str
            Attribute name to get the value for.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.get_attribute", self._impl_obj.get_attribute(name=name)
            )
        )

    async def text_content(self) -> typing.Optional[str]:
        """ElementHandle.text_content

        Returns the `node.textContent`.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.text_content", self._impl_obj.text_content()
            )
        )

    async def inner_text(self) -> str:
        """ElementHandle.inner_text

        Returns the `element.innerText`.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.inner_text", self._impl_obj.inner_text())
        )

    async def inner_html(self) -> str:
        """ElementHandle.inner_html

        Returns the `element.innerHTML`.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.inner_html", self._impl_obj.inner_html())
        )

    async def is_checked(self) -> bool:
        """ElementHandle.is_checked

        Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.is_checked", self._impl_obj.is_checked())
        )

    async def is_disabled(self) -> bool:
        """ElementHandle.is_disabled

        Returns whether the element is disabled, the opposite of [enabled](./actionability.md#enabled).

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.is_disabled", self._impl_obj.is_disabled()
            )
        )

    async def is_editable(self) -> bool:
        """ElementHandle.is_editable

        Returns whether the element is [editable](./actionability.md#editable).

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.is_editable", self._impl_obj.is_editable()
            )
        )

    async def is_enabled(self) -> bool:
        """ElementHandle.is_enabled

        Returns whether the element is [enabled](./actionability.md#enabled).

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.is_enabled", self._impl_obj.is_enabled())
        )

    async def is_hidden(self) -> bool:
        """ElementHandle.is_hidden

        Returns whether the element is hidden, the opposite of [visible](./actionability.md#visible).

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.is_hidden", self._impl_obj.is_hidden())
        )

    async def is_visible(self) -> bool:
        """ElementHandle.is_visible

        Returns whether the element is [visible](./actionability.md#visible).

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.is_visible", self._impl_obj.is_visible())
        )

    async def dispatch_event(
        self, type: str, event_init: typing.Dict = None
    ) -> NoneType:
        """ElementHandle.dispatch_event

        The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the elment, `click`
        is dispatched. This is equivalend to calling
        [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

        ```py
        await element_handle.dispatch_event(\"click\")
        ```

        Under the hood, it creates an instance of an event based on the given `type`, initializes it with `eventInit` properties
        and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

        Since `eventInit` is event-specific, please refer to the events documentation for the lists of initial properties:
        - [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
        - [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
        - [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
        - [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
        - [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
        - [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
        - [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

        You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

        ```py
        # note you can only create data_transfer in chromium and firefox
        data_transfer = await page.evaluate_handle(\"new DataTransfer()\")
        await element_handle.dispatch_event(\"#source\", \"dragstart\", {\"dataTransfer\": data_transfer})
        ```

        Parameters
        ----------
        type : str
            DOM event type: `"click"`, `"dragstart"`, etc.
        event_init : Union[Dict, NoneType]
            Optional event-specific initialization properties.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.dispatch_event",
                self._impl_obj.dispatch_event(
                    type=type, eventInit=mapping.to_impl(event_init)
                ),
            )
        )

    async def scroll_into_view_if_needed(self, *, timeout: float = None) -> NoneType:
        """ElementHandle.scroll_into_view_if_needed

        This method waits for [actionability](./actionability.md) checks, then tries to scroll element into view, unless it is
        completely visible as defined by
        [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

        Throws when `elementHandle` does not point to an element
        [connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.scroll_into_view_if_needed",
                self._impl_obj.scroll_into_view_if_needed(timeout=timeout),
            )
        )

    async def hover(
        self,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        timeout: float = None,
        force: bool = None
    ) -> NoneType:
        """ElementHandle.hover

        This method hovers over the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to hover over the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.hover",
                self._impl_obj.hover(
                    modifiers=modifiers, position=position, timeout=timeout, force=force
                ),
            )
        )

    async def click(
        self,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.click

        This method clicks the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.click",
                self._impl_obj.click(
                    modifiers=modifiers,
                    position=position,
                    delay=delay,
                    button=button,
                    clickCount=click_count,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def dblclick(
        self,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.dblclick

        This method double clicks the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to double click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set. Note that if the
           first click of the `dblclick()` triggers a navigation event, this method will reject.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > NOTE: `elementHandle.dblclick()` dispatches two `click` events and a single `dblclick` event.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.dblclick",
                self._impl_obj.dblclick(
                    modifiers=modifiers,
                    position=position,
                    delay=delay,
                    button=button,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def select_option(
        self,
        value: typing.Union[str, typing.List[str]] = None,
        *,
        index: typing.Union[int, typing.List[int]] = None,
        label: typing.Union[str, typing.List[str]] = None,
        element: typing.Union["ElementHandle", typing.List["ElementHandle"]] = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> typing.List[str]:
        """ElementHandle.select_option

        Returns the array of option values that have been successfully selected.

        Triggers a `change` and `input` event once all the provided options have been selected. If element is not a `<select>`
        element, the method throws an error.

        Will wait until all specified options are present in the `<select>` element.

        ```py
        # single selection matching the value
        await handle.select_option(\"blue\")
        # single selection matching the label
        await handle.select_option(label=\"blue\")
        # multiple selection
        await handle.select_option(value=[\"red\", \"green\", \"blue\"])
        ```

        Parameters
        ----------
        value : Union[List[str], str, NoneType]
            Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise
            only the first option matching one of the passed options is selected. Optional.
        index : Union[List[int], int, NoneType]
            Options to select by index. Optional.
        label : Union[List[str], str, NoneType]
            Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise
            only the first option matching one of the passed options is selected. Optional.
        element : Union[ElementHandle, List[ElementHandle], NoneType]
            Option elements to select. Optional.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.

        Returns
        -------
        List[str]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.select_option",
                self._impl_obj.select_option(
                    value=value,
                    index=index,
                    label=label,
                    element=mapping.to_impl(element),
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def tap(
        self,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.tap

        This method taps the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > NOTE: `elementHandle.tap()` requires that the `hasTouch` option of the browser context be set to true.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.tap",
                self._impl_obj.tap(
                    modifiers=modifiers,
                    position=position,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def fill(
        self, value: str, *, timeout: float = None, no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.fill

        This method waits for [actionability](./actionability.md) checks, focuses the element, fills it and triggers an `input`
        event after filling. If the element is inside the `<label>` element that has associated
        [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), that control will be filled
        instead. If the element to be filled is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method
        throws an error. Note that you can pass an empty string to clear the input field.

        Parameters
        ----------
        value : str
            Value to set for the `<input>`, `<textarea>` or `[contenteditable]` element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.fill",
                self._impl_obj.fill(
                    value=value, timeout=timeout, noWaitAfter=no_wait_after
                ),
            )
        )

    async def select_text(self, *, timeout: float = None) -> NoneType:
        """ElementHandle.select_text

        This method waits for [actionability](./actionability.md) checks, then focuses the element and selects all its text
        content.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.select_text",
                self._impl_obj.select_text(timeout=timeout),
            )
        )

    async def set_input_files(
        self,
        files: typing.Union[
            str,
            pathlib.Path,
            FilePayload,
            typing.List[typing.Union[str, pathlib.Path]],
            typing.List[FilePayload],
        ],
        *,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.set_input_files

        This method expects `elementHandle` to point to an
        [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

        Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they
        are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        files : Union[List[Union[pathlib.Path, str]], List[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.set_input_files",
                self._impl_obj.set_input_files(
                    files=files, timeout=timeout, noWaitAfter=no_wait_after
                ),
            )
        )

    async def focus(self) -> NoneType:
        """ElementHandle.focus

        Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.
        """

        return mapping.from_maybe_impl(
            await self._async("element_handle.focus", self._impl_obj.focus())
        )

    async def type(
        self,
        text: str,
        *,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.type

        Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

        To press a special key, like `Control` or `ArrowDown`, use `element_handle.press()`.

        ```py
        await element_handle.type(\"hello\") # types instantly
        await element_handle.type(\"world\", delay=100) # types slower, like a user
        ```

        An example of typing into a text field and then submitting the form:

        ```py
        element_handle = await page.query_selector(\"input\")
        await element_handle.type(\"some text\")
        await element_handle.press(\"Enter\")
        ```

        Parameters
        ----------
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.type",
                self._impl_obj.type(
                    text=text, delay=delay, timeout=timeout, noWaitAfter=no_wait_after
                ),
            )
        )

    async def press(
        self,
        key: str,
        *,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.press

        Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: \"Control+o\"` or `key: \"Control+Shift+T\"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.press",
                self._impl_obj.press(
                    key=key, delay=delay, timeout=timeout, noWaitAfter=no_wait_after
                ),
            )
        )

    async def check(
        self, *, timeout: float = None, force: bool = None, no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.check

        This method checks the element by performing the following steps:
        1. Ensure that element is a checkbox or a radio input. If not, this method rejects. If the element is already
           checked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now checked. If not, this method rejects.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.check",
                self._impl_obj.check(
                    timeout=timeout, force=force, noWaitAfter=no_wait_after
                ),
            )
        )

    async def uncheck(
        self, *, timeout: float = None, force: bool = None, no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.uncheck

        This method checks the element by performing the following steps:
        1. Ensure that element is a checkbox or a radio input. If not, this method rejects. If the element is already
           unchecked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now unchecked. If not, this method rejects.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.uncheck",
                self._impl_obj.uncheck(
                    timeout=timeout, force=force, noWaitAfter=no_wait_after
                ),
            )
        )

    async def bounding_box(self) -> typing.Optional[FloatRect]:
        """ElementHandle.bounding_box

        This method returns the bounding box of the element, or `null` if the element is not visible. The bounding box is
        calculated relative to the main frame viewport - which is usually the same as the browser window.

        Scrolling affects the returned bonding box, similarly to
        [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). That
        means `x` and/or `y` may be negative.

        Elements from child frames return the bounding box relative to the main frame, unlike the
        [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

        Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the following
        snippet should click the center of the element.

        ```py
        box = await element_handle.bounding_box()
        await page.mouse.click(box[\"x\"] + box[\"width\"] / 2, box[\"y\"] + box[\"height\"] / 2)
        ```

        Returns
        -------
        Union[{x: float, y: float, width: float, height: float}, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "element_handle.bounding_box", self._impl_obj.bounding_box()
            )
        )

    async def screenshot(
        self,
        *,
        timeout: float = None,
        type: Literal["jpeg", "png"] = None,
        path: typing.Union[str, pathlib.Path] = None,
        quality: int = None,
        omit_background: bool = None
    ) -> bytes:
        """ElementHandle.screenshot

        Returns the buffer with the captured screenshot.

        This method waits for the [actionability](./actionability.md) checks, then scrolls element into view before taking a
        screenshot. If the element is detached from DOM, the method throws an error.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        type : Union["jpeg", "png", NoneType]
            Specify screenshot type, defaults to `png`.
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the image to. The screenshot type will be inferred from file extension. If `path` is a relative
            path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to
            the disk.
        quality : Union[int, NoneType]
            The quality of the image, between 0-100. Not applicable to `png` images.
        omit_background : Union[bool, NoneType]
            Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images.
            Defaults to `false`.

        Returns
        -------
        bytes
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.screenshot",
                self._impl_obj.screenshot(
                    timeout=timeout,
                    type=type,
                    path=path,
                    quality=quality,
                    omitBackground=omit_background,
                ),
            )
        )

    async def query_selector(self, selector: str) -> typing.Optional["ElementHandle"]:
        """ElementHandle.query_selector

        The method finds an element matching the specified selector in the `ElementHandle`'s subtree. See
        [Working with selectors](./selectors.md) for more details. If no elements match the selector, returns `null`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "element_handle.query_selector",
                self._impl_obj.query_selector(selector=selector),
            )
        )

    async def query_selector_all(self, selector: str) -> typing.List["ElementHandle"]:
        """ElementHandle.query_selector_all

        The method finds all elements matching the specified selector in the `ElementHandle`s subtree. See
        [Working with selectors](./selectors.md) for more details. If no elements match the selector, returns empty array.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.

        Returns
        -------
        List[ElementHandle]
        """

        return mapping.from_impl_list(
            await self._async(
                "element_handle.query_selector_all",
                self._impl_obj.query_selector_all(selector=selector),
            )
        )

    async def eval_on_selector(
        self, selector: str, expression: str, arg: typing.Any = None
    ) -> typing.Any:
        """ElementHandle.eval_on_selector

        Returns the return value of `expression`.

        The method finds an element matching the specified selector in the `ElementHandle`s subtree and passes it as a first
        argument to `expression`. See [Working with selectors](./selectors.md) for more details. If no elements match the
        selector, the method throws an error.

        If `expression` returns a [Promise], then `element_handle.eval_on_selector()` would wait for the promise to resolve
        and return its value.

        Examples:

        ```py
        tweet_handle = await page.query_selector(\".tweet\")
        assert await tweet_handle.eval_on_selector(\".like\", \"node => node.innerText\") == \"100\"
        assert await tweet_handle.eval_on_selector(\".retweets\", \"node => node.innerText\") = \"10\"
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.eval_on_selector",
                self._impl_obj.eval_on_selector(
                    selector=selector, expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def eval_on_selector_all(
        self, selector: str, expression: str, arg: typing.Any = None
    ) -> typing.Any:
        """ElementHandle.eval_on_selector_all

        Returns the return value of `expression`.

        The method finds all elements matching the specified selector in the `ElementHandle`'s subtree and passes an array of
        matched elements as a first argument to `expression`. See [Working with selectors](./selectors.md) for more details.

        If `expression` returns a [Promise], then `element_handle.eval_on_selector_all()` would wait for the promise to
        resolve and return its value.

        Examples:

        ```html
        <div class=\"feed\">
          <div class=\"tweet\">Hello!</div>
          <div class=\"tweet\">Hi!</div>
        </div>
        ```

        ```py
        feed_handle = await page.query_selector(\".feed\")
        assert await feed_handle.eval_on_selector_all(\".tweet\", \"nodes => nodes.map(n => n.innerText)\") == [\"hello!\", \"hi!\"]
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.eval_on_selector_all",
                self._impl_obj.eval_on_selector_all(
                    selector=selector, expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def wait_for_element_state(
        self,
        state: Literal[
            "disabled", "editable", "enabled", "hidden", "stable", "visible"
        ],
        *,
        timeout: float = None
    ) -> NoneType:
        """ElementHandle.wait_for_element_state

        Returns when the element satisfies the `state`.

        Depending on the `state` parameter, this method waits for one of the [actionability](./actionability.md) checks to pass.
        This method throws when the element is detached while waiting, unless waiting for the `\"hidden\"` state.
        - `\"visible\"` Wait until the element is [visible](./actionability.md#visible).
        - `\"hidden\"` Wait until the element is [not visible](./actionability.md#visible) or
          [not attached](./actionability.md#attached). Note that waiting for hidden does not throw when the element detaches.
        - `\"stable\"` Wait until the element is both [visible](./actionability.md#visible) and
          [stable](./actionability.md#stable).
        - `\"enabled\"` Wait until the element is [enabled](./actionability.md#enabled).
        - `\"disabled\"` Wait until the element is [not enabled](./actionability.md#enabled).
        - `\"editable\"` Wait until the element is [editable](./actionability.md#editable).

        If the element does not satisfy the condition for the `timeout` milliseconds, this method will throw.

        Parameters
        ----------
        state : Union["disabled", "editable", "enabled", "hidden", "stable", "visible"]
            A state to wait for, see below for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "element_handle.wait_for_element_state",
                self._impl_obj.wait_for_element_state(state=state, timeout=timeout),
            )
        )

    async def wait_for_selector(
        self,
        selector: str,
        *,
        state: Literal["attached", "detached", "hidden", "visible"] = None,
        timeout: float = None
    ) -> typing.Optional["ElementHandle"]:
        """ElementHandle.wait_for_selector

        Returns element specified by selector when it satisfies `state` option. Returns `null` if waiting for `hidden` or
        `detached`.

        Wait for the `selector` relative to the element handle to satisfy `state` option (either appear/disappear from dom, or
        become visible/hidden). If at the moment of calling the method `selector` already satisfies the condition, the method
        will return immediately. If the selector doesn't satisfy the condition for the `timeout` milliseconds, the function will
        throw.

        ```py
        await page.set_content(\"<div><span></span></div>\")
        div = await page.query_selector(\"div\")
        # waiting for the \"span\" selector relative to the div.
        span = await div.wait_for_selector(\"span\", state=\"attached\")
        ```

        > NOTE: This method does not work across navigations, use `page.wait_for_selector()` instead.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        state : Union["attached", "detached", "hidden", "visible", NoneType]
            Defaults to `'visible'`. Can be either:
            - `'attached'` - wait for element to be present in DOM.
            - `'detached'` - wait for element to not be present in DOM.
            - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without
              any content or with `display:none` has an empty bounding box and is not considered visible.
            - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`.
              This is opposite to the `'visible'` option.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "element_handle.wait_for_selector",
                self._impl_obj.wait_for_selector(
                    selector=selector, state=state, timeout=timeout
                ),
            )
        )


mapping.register(ElementHandleImpl, ElementHandle)


class Accessibility(AsyncBase):
    def __init__(self, obj: AccessibilityImpl):
        super().__init__(obj)

    async def snapshot(
        self, *, interesting_only: bool = None, root: "ElementHandle" = None
    ) -> typing.Optional[typing.Dict]:
        """Accessibility.snapshot

        Captures the current state of the accessibility tree. The returned object represents the root accessible node of the
        page.

        > NOTE: The Chromium accessibility tree contains nodes that go unused on most platforms and by most screen readers.
        Playwright will discard them as well for an easier to process tree, unless `interestingOnly` is set to `false`.

        An example of dumping the entire accessibility tree:

        ```py
        snapshot = await page.accessibility.snapshot()
        print(snapshot)
        ```

        An example of logging the focused node's name:

        ```py
        def find_focused_node(node):
            if (node.get(\"focused\"))
                return node
            for child in (node.get(\"children\") or []):
                found_node = find_focused_node(child)
                return found_node
            return None

        snapshot = await page.accessibility.snapshot()
        node = find_focused_node(snapshot)
        if node:
            print(node[\"name\"])
        ```

        Parameters
        ----------
        interesting_only : Union[bool, NoneType]
            Prune uninteresting nodes from the tree. Defaults to `true`.
        root : Union[ElementHandle, NoneType]
            The root DOM element for the snapshot. Defaults to the whole page.

        Returns
        -------
        Union[Dict, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "accessibility.snapshot",
                self._impl_obj.snapshot(
                    interestingOnly=interesting_only, root=mapping.to_impl(root)
                ),
            )
        )


mapping.register(AccessibilityImpl, Accessibility)


class FileChooser(AsyncBase):
    def __init__(self, obj: FileChooserImpl):
        super().__init__(obj)

    @property
    def page(self) -> "Page":
        """FileChooser.page

        Returns page this file chooser belongs to.

        Returns
        -------
        Page
        """
        return mapping.from_impl(self._impl_obj.page)

    @property
    def element(self) -> "ElementHandle":
        """FileChooser.element

        Returns input element associated with this file chooser.

        Returns
        -------
        ElementHandle
        """
        return mapping.from_impl(self._impl_obj.element)

    def is_multiple(self) -> bool:
        """FileChooser.is_multiple

        Returns whether this file chooser accepts multiple files.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(self._impl_obj.is_multiple())

    async def set_files(
        self,
        files: typing.Union[
            str,
            pathlib.Path,
            FilePayload,
            typing.List[typing.Union[str, pathlib.Path]],
            typing.List[FilePayload],
        ],
        *,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """FileChooser.set_files

        Sets the value of the file input this chooser is associated with. If some of the `filePaths` are relative paths, then
        they are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        files : Union[List[Union[pathlib.Path, str]], List[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "file_chooser.set_files",
                self._impl_obj.set_files(
                    files=files, timeout=timeout, noWaitAfter=no_wait_after
                ),
            )
        )


mapping.register(FileChooserImpl, FileChooser)


class Frame(AsyncBase):
    def __init__(self, obj: FrameImpl):
        super().__init__(obj)

    @property
    def page(self) -> "Page":
        """Frame.page

        Returns the page containing this frame.

        Returns
        -------
        Page
        """
        return mapping.from_impl(self._impl_obj.page)

    @property
    def name(self) -> str:
        """Frame.name

        Returns frame's name attribute as specified in the tag.

        If the name is empty, returns the id attribute instead.

        > NOTE: This value is calculated once when the frame is created, and will not update if the attribute is changed later.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.name)

    @property
    def url(self) -> str:
        """Frame.url

        Returns frame's url.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def parent_frame(self) -> typing.Optional["Frame"]:
        """Frame.parent_frame

        Parent frame, if any. Detached frames and main frames return `null`.

        Returns
        -------
        Union[Frame, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.parent_frame)

    @property
    def child_frames(self) -> typing.List["Frame"]:
        """Frame.child_frames

        Returns
        -------
        List[Frame]
        """
        return mapping.from_impl_list(self._impl_obj.child_frames)

    async def goto(
        self,
        url: str,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        referer: str = None
    ) -> typing.Optional["Response"]:
        """Frame.goto

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect.

        `frame.goto` will throw an error if:
        - there's an SSL error (e.g. in case of self-signed certificates).
        - target URL is invalid.
        - the `timeout` is exceeded during navigation.
        - the remote server does not respond or is unreachable.
        - the main resource failed to load.

        `frame.goto` will not throw an error when any valid HTTP status code is returned by the remote server, including 404
        \"Not Found\" and 500 \"Internal Server Error\".  The status code for such responses can be retrieved by calling
        `response.status()`.

        > NOTE: `frame.goto` either throws an error or returns a main resource response. The only exceptions are navigation to
        `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.
        > NOTE: Headless mode doesn't support navigation to a PDF document. See the
        [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

        Parameters
        ----------
        url : str
            URL to navigate frame to. The url should include scheme, e.g. `https://`.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        referer : Union[str, NoneType]
            Referer header value. If provided it will take preference over the referer header value set by
            `page.set_extra_http_headers()`.

        Returns
        -------
        Union[Response, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "frame.goto",
                self._impl_obj.goto(
                    url=url, timeout=timeout, waitUntil=wait_until, referer=referer
                ),
            )
        )

    def expect_navigation(
        self,
        *,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None
    ) -> AsyncEventContextManager["Response"]:
        """Frame.expect_navigation

        Waits for the frame navigation and returns the main resource response. In case of multiple redirects, the navigation
        will resolve with the response of the last redirect. In case of navigation to a different anchor or navigation due to
        History API usage, the navigation will resolve with `null`.

        This method waits for the frame to navigate to a new URL. It is useful for when you run code which will indirectly cause
        the frame to navigate. Consider this example:

        ```py
        async with frame.expect_navigation():
            await frame.click(\"a.delayed-navigation\") # clicking the link will indirectly cause a navigation
        # Resolves after navigation has finished
        ```

        > NOTE: Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is
        considered a navigation.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str, NoneType]
            A glob pattern, regex pattern or predicate receiving [URL] to match while waiting for the navigation.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.

        Returns
        -------
        EventContextManager[Response]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_navigation(
                url=self._wrap_handler(url), wait_until=wait_until, timeout=timeout
            ).future
        )

    async def wait_for_load_state(
        self,
        state: Literal["domcontentloaded", "load", "networkidle"] = None,
        *,
        timeout: float = None
    ) -> NoneType:
        """Frame.wait_for_load_state

        Waits for the required load state to be reached.

        This returns when the frame reaches a required load state, `load` by default. The navigation must have been committed
        when this method is called. If current document has already reached the required state, resolves immediately.

        ```py
        await frame.click(\"button\") # click triggers navigation.
        await frame.wait_for_load_state() # the promise resolves after \"load\" event.
        ```

        Parameters
        ----------
        state : Union["domcontentloaded", "load", "networkidle", NoneType]
            Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current
            document, the method resolves immediately. Can be one of:
            - `'load'` - wait for the `load` event to be fired.
            - `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired.
            - `'networkidle'` - wait until there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.wait_for_load_state",
                self._impl_obj.wait_for_load_state(state=state, timeout=timeout),
            )
        )

    async def frame_element(self) -> "ElementHandle":
        """Frame.frame_element

        Returns the `frame` or `iframe` element handle which corresponds to this frame.

        This is an inverse of `element_handle.content_frame()`. Note that returned handle actually belongs to the parent
        frame.

        This method throws an error if the frame has been detached before `frameElement()` returns.

        ```py
        frame_element = await frame.frame_element()
        content_frame = await frame_element.content_frame()
        assert frame == content_frame
        ```

        Returns
        -------
        ElementHandle
        """

        return mapping.from_impl(
            await self._async("frame.frame_element", self._impl_obj.frame_element())
        )

    async def evaluate(self, expression: str, arg: typing.Any = None) -> typing.Any:
        """Frame.evaluate

        Returns the return value of `expression`.

        If the function passed to the `frame.evaluate()` returns a [Promise], then `frame.evaluate()` would wait
        for the promise to resolve and return its value.

        If the function passed to the `frame.evaluate()` returns a non-[Serializable] value, then
        `frame.evaluate()` returns `undefined`. Playwright also supports transferring some additional values that are
        not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

        ```py
        result = await frame.evaluate(\"([x, y]) => Promise.resolve(x * y)\", [7, 8])
        print(result) # prints \"56\"
        ```

        A string can also be passed in instead of a function.

        ```py
        print(await frame.evaluate(\"1 + 2\")) # prints \"3\"
        x = 10
        print(await frame.evaluate(f\"1 + {x}\")) # prints \"11\"
        ```

        `ElementHandle` instances can be passed as an argument to the `frame.evaluate()`:

        ```py
        body_handle = await frame.query_selector(\"body\")
        html = await frame.evaluate(\"([body, suffix]) => body.innerHTML + suffix\", [body_handle, \"hello\"])
        await body_handle.dispose()
        ```

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.evaluate",
                self._impl_obj.evaluate(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def evaluate_handle(
        self, expression: str, arg: typing.Any = None
    ) -> "JSHandle":
        """Frame.evaluate_handle

        Returns the return value of `expression` as a `JSHandle`.

        The only difference between `frame.evaluate()` and `frame.evaluate_handle()` is that
        `frame.evaluate_handle()` returns `JSHandle`.

        If the function, passed to the `frame.evaluate_handle()`, returns a [Promise], then
        `frame.evaluate_handle()` would wait for the promise to resolve and return its value.

        ```py
        a_window_handle = await frame.evaluate_handle(\"Promise.resolve(window)\")
        a_window_handle # handle for the window object.
        ```

        A string can also be passed in instead of a function.

        ```py
        a_handle = await page.evaluate_handle(\"document\") # handle for the \"document\"
        ```

        `JSHandle` instances can be passed as an argument to the `frame.evaluate_handle()`:

        ```py
        a_handle = await page.evaluate_handle(\"document.body\")
        result_handle = await page.evaluate_handle(\"body => body.innerHTML\", a_handle)
        print(await result_handle.json_value())
        await result_handle.dispose()
        ```

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "frame.evaluate_handle",
                self._impl_obj.evaluate_handle(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def query_selector(self, selector: str) -> typing.Optional["ElementHandle"]:
        """Frame.query_selector

        Returns the ElementHandle pointing to the frame element.

        The method finds an element matching the specified selector within the frame. See
        [Working with selectors](./selectors.md) for more details. If no elements match the selector, returns `null`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "frame.query_selector", self._impl_obj.query_selector(selector=selector)
            )
        )

    async def query_selector_all(self, selector: str) -> typing.List["ElementHandle"]:
        """Frame.query_selector_all

        Returns the ElementHandles pointing to the frame elements.

        The method finds all elements matching the specified selector within the frame. See
        [Working with selectors](./selectors.md) for more details. If no elements match the selector, returns empty array.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.

        Returns
        -------
        List[ElementHandle]
        """

        return mapping.from_impl_list(
            await self._async(
                "frame.query_selector_all",
                self._impl_obj.query_selector_all(selector=selector),
            )
        )

    async def wait_for_selector(
        self,
        selector: str,
        *,
        timeout: float = None,
        state: Literal["attached", "detached", "hidden", "visible"] = None
    ) -> typing.Optional["ElementHandle"]:
        """Frame.wait_for_selector

        Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
        `detached`.

        Wait for the `selector` to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If at
        the moment of calling the method `selector` already satisfies the condition, the method will return immediately. If the
        selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

        This method works across navigations:

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            chromium = playwright.chromium
            browser = await chromium.launch()
            page = await browser.new_page()
            for current_url in [\"https://google.com\", \"https://bbc.com\"]:
                await page.goto(current_url, wait_until=\"domcontentloaded\")
                element = await page.main_frame.wait_for_selector(\"img\")
                print(\"Loaded image: \" + str(await element.get_attribute(\"src\")))
            await browser.close()

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        state : Union["attached", "detached", "hidden", "visible", NoneType]
            Defaults to `'visible'`. Can be either:
            - `'attached'` - wait for element to be present in DOM.
            - `'detached'` - wait for element to not be present in DOM.
            - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without
              any content or with `display:none` has an empty bounding box and is not considered visible.
            - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`.
              This is opposite to the `'visible'` option.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "frame.wait_for_selector",
                self._impl_obj.wait_for_selector(
                    selector=selector, timeout=timeout, state=state
                ),
            )
        )

    async def is_checked(self, selector: str, *, timeout: float = None) -> bool:
        """Frame.is_checked

        Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.is_checked",
                self._impl_obj.is_checked(selector=selector, timeout=timeout),
            )
        )

    async def is_disabled(self, selector: str, *, timeout: float = None) -> bool:
        """Frame.is_disabled

        Returns whether the element is disabled, the opposite of [enabled](./actionability.md#enabled).

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.is_disabled",
                self._impl_obj.is_disabled(selector=selector, timeout=timeout),
            )
        )

    async def is_editable(self, selector: str, *, timeout: float = None) -> bool:
        """Frame.is_editable

        Returns whether the element is [editable](./actionability.md#editable).

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.is_editable",
                self._impl_obj.is_editable(selector=selector, timeout=timeout),
            )
        )

    async def is_enabled(self, selector: str, *, timeout: float = None) -> bool:
        """Frame.is_enabled

        Returns whether the element is [enabled](./actionability.md#enabled).

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.is_enabled",
                self._impl_obj.is_enabled(selector=selector, timeout=timeout),
            )
        )

    async def is_hidden(self, selector: str, *, timeout: float = None) -> bool:
        """Frame.is_hidden

        Returns whether the element is hidden, the opposite of [visible](./actionability.md#visible).  `selector` that does not
        match any elements is considered hidden.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.is_hidden",
                self._impl_obj.is_hidden(selector=selector, timeout=timeout),
            )
        )

    async def is_visible(self, selector: str, *, timeout: float = None) -> bool:
        """Frame.is_visible

        Returns whether the element is [visible](./actionability.md#visible). `selector` that does not match any elements is
        considered not visible.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.is_visible",
                self._impl_obj.is_visible(selector=selector, timeout=timeout),
            )
        )

    async def dispatch_event(
        self,
        selector: str,
        type: str,
        event_init: typing.Dict = None,
        *,
        timeout: float = None
    ) -> NoneType:
        """Frame.dispatch_event

        The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the elment, `click`
        is dispatched. This is equivalend to calling
        [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

        ```py
        await frame.dispatch_event(\"button#submit\", \"click\")
        ```

        Under the hood, it creates an instance of an event based on the given `type`, initializes it with `eventInit` properties
        and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

        Since `eventInit` is event-specific, please refer to the events documentation for the lists of initial properties:
        - [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
        - [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
        - [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
        - [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
        - [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
        - [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
        - [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

        You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

        ```py
        # note you can only create data_transfer in chromium and firefox
        data_transfer = await frame.evaluate_handle(\"new DataTransfer()\")
        await frame.dispatch_event(\"#source\", \"dragstart\", { \"dataTransfer\": data_transfer })
        ```

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        type : str
            DOM event type: `"click"`, `"dragstart"`, etc.
        event_init : Union[Dict, NoneType]
            Optional event-specific initialization properties.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.dispatch_event",
                self._impl_obj.dispatch_event(
                    selector=selector,
                    type=type,
                    eventInit=mapping.to_impl(event_init),
                    timeout=timeout,
                ),
            )
        )

    async def eval_on_selector(
        self, selector: str, expression: str, arg: typing.Any = None
    ) -> typing.Any:
        """Frame.eval_on_selector

        Returns the return value of `expression`.

        The method finds an element matching the specified selector within the frame and passes it as a first argument to
        `expression`. See [Working with selectors](./selectors.md) for more details. If no elements match the selector, the
        method throws an error.

        If `expression` returns a [Promise], then `frame.eval_on_selector()` would wait for the promise to resolve and
        return its value.

        Examples:

        ```py
        search_value = await frame.eval_on_selector(\"#search\", \"el => el.value\")
        preload_href = await frame.eval_on_selector(\"link[rel=preload]\", \"el => el.href\")
        html = await frame.eval_on_selector(\".main-container\", \"(e, suffix) => e.outerHTML + suffix\", \"hello\")
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.eval_on_selector",
                self._impl_obj.eval_on_selector(
                    selector=selector, expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def eval_on_selector_all(
        self, selector: str, expression: str, arg: typing.Any = None
    ) -> typing.Any:
        """Frame.eval_on_selector_all

        Returns the return value of `expression`.

        The method finds all elements matching the specified selector within the frame and passes an array of matched elements
        as a first argument to `expression`. See [Working with selectors](./selectors.md) for more details.

        If `expression` returns a [Promise], then `frame.eval_on_selector_all()` would wait for the promise to resolve and
        return its value.

        Examples:

        ```py
        divs_counts = await frame.eval_on_selector_all(\"div\", \"(divs, min) => divs.length >= min\", 10)
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.eval_on_selector_all",
                self._impl_obj.eval_on_selector_all(
                    selector=selector, expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def content(self) -> str:
        """Frame.content

        Gets the full HTML contents of the frame, including the doctype.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("frame.content", self._impl_obj.content())
        )

    async def set_content(
        self,
        html: str,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None
    ) -> NoneType:
        """Frame.set_content

        Parameters
        ----------
        html : str
            HTML markup to assign to the page.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.set_content",
                self._impl_obj.set_content(
                    html=html, timeout=timeout, waitUntil=wait_until
                ),
            )
        )

    def is_detached(self) -> bool:
        """Frame.is_detached

        Returns `true` if the frame has been detached, or `false` otherwise.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(self._impl_obj.is_detached())

    async def add_script_tag(
        self,
        *,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None,
        type: str = None
    ) -> "ElementHandle":
        """Frame.add_script_tag

        Returns the added tag when the script's onload fires or when the script content was injected into frame.

        Adds a `<script>` tag into the page with the desired url or content.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of a script to be added.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory.
        content : Union[str, NoneType]
            Raw JavaScript content to be injected into frame.
        type : Union[str, NoneType]
            Script type. Use 'module' in order to load a Javascript ES6 module. See
            [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details.

        Returns
        -------
        ElementHandle
        """

        return mapping.from_impl(
            await self._async(
                "frame.add_script_tag",
                self._impl_obj.add_script_tag(
                    url=url, path=path, content=content, type=type
                ),
            )
        )

    async def add_style_tag(
        self,
        *,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None
    ) -> "ElementHandle":
        """Frame.add_style_tag

        Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

        Adds a `<link rel=\"stylesheet\">` tag into the page with the desired url or a `<style type=\"text/css\">` tag with the
        content.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of the `<link>` tag.
        path : Union[pathlib.Path, str, NoneType]
            Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory.
        content : Union[str, NoneType]
            Raw CSS content to be injected into frame.

        Returns
        -------
        ElementHandle
        """

        return mapping.from_impl(
            await self._async(
                "frame.add_style_tag",
                self._impl_obj.add_style_tag(url=url, path=path, content=content),
            )
        )

    async def click(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.click

        This method clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.click",
                self._impl_obj.click(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    delay=delay,
                    button=button,
                    clickCount=click_count,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def dblclick(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.dblclick

        This method double clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to double click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set. Note that if the
           first click of the `dblclick()` triggers a navigation event, this method will reject.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > NOTE: `frame.dblclick()` dispatches two `click` events and a single `dblclick` event.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.dblclick",
                self._impl_obj.dblclick(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    delay=delay,
                    button=button,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def tap(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.tap

        This method taps an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > NOTE: `frame.tap()` requires that the `hasTouch` option of the browser context be set to true.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.tap",
                self._impl_obj.tap(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def fill(
        self,
        selector: str,
        value: str,
        *,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.fill

        This method waits for an element matching `selector`, waits for [actionability](./actionability.md) checks, focuses the
        element, fills it and triggers an `input` event after filling. If the element is inside the `<label>` element that has
        associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), that control will be
        filled instead. If the element to be filled is not an `<input>`, `<textarea>` or `[contenteditable]` element, this
        method throws an error. Note that you can pass an empty string to clear the input field.

        To send fine-grained keyboard events, use `frame.type()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        value : str
            Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.fill",
                self._impl_obj.fill(
                    selector=selector,
                    value=value,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def focus(self, selector: str, *, timeout: float = None) -> NoneType:
        """Frame.focus

        This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the method
        waits until a matching element appears in the DOM.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.focus", self._impl_obj.focus(selector=selector, timeout=timeout)
            )
        )

    async def text_content(
        self, selector: str, *, timeout: float = None
    ) -> typing.Optional[str]:
        """Frame.text_content

        Returns `element.textContent`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.text_content",
                self._impl_obj.text_content(selector=selector, timeout=timeout),
            )
        )

    async def inner_text(self, selector: str, *, timeout: float = None) -> str:
        """Frame.inner_text

        Returns `element.innerText`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.inner_text",
                self._impl_obj.inner_text(selector=selector, timeout=timeout),
            )
        )

    async def inner_html(self, selector: str, *, timeout: float = None) -> str:
        """Frame.inner_html

        Returns `element.innerHTML`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.inner_html",
                self._impl_obj.inner_html(selector=selector, timeout=timeout),
            )
        )

    async def get_attribute(
        self, selector: str, name: str, *, timeout: float = None
    ) -> typing.Optional[str]:
        """Frame.get_attribute

        Returns element attribute value.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        name : str
            Attribute name to get the value for.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.get_attribute",
                self._impl_obj.get_attribute(
                    selector=selector, name=name, timeout=timeout
                ),
            )
        )

    async def hover(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        timeout: float = None,
        force: bool = None
    ) -> NoneType:
        """Frame.hover

        This method hovers over an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to hover over the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.hover",
                self._impl_obj.hover(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    timeout=timeout,
                    force=force,
                ),
            )
        )

    async def select_option(
        self,
        selector: str,
        value: typing.Union[str, typing.List[str]] = None,
        *,
        index: typing.Union[int, typing.List[int]] = None,
        label: typing.Union[str, typing.List[str]] = None,
        element: typing.Union["ElementHandle", typing.List["ElementHandle"]] = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> typing.List[str]:
        """Frame.select_option

        Returns the array of option values that have been successfully selected.

        Triggers a `change` and `input` event once all the provided options have been selected. If there's no `<select>` element
        matching `selector`, the method throws an error.

        Will wait until all specified options are present in the `<select>` element.

        ```py
        # single selection matching the value
        await frame.select_option(\"select#colors\", \"blue\")
        # single selection matching the label
        await frame.select_option(\"select#colors\", label=\"blue\")
        # multiple selection
        await frame.select_option(\"select#colors\", value=[\"red\", \"green\", \"blue\"])
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        value : Union[List[str], str, NoneType]
            Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise
            only the first option matching one of the passed options is selected. Optional.
        index : Union[List[int], int, NoneType]
            Options to select by index. Optional.
        label : Union[List[str], str, NoneType]
            Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise
            only the first option matching one of the passed options is selected. Optional.
        element : Union[ElementHandle, List[ElementHandle], NoneType]
            Option elements to select. Optional.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.

        Returns
        -------
        List[str]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.select_option",
                self._impl_obj.select_option(
                    selector=selector,
                    value=value,
                    index=index,
                    label=label,
                    element=mapping.to_impl(element),
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def set_input_files(
        self,
        selector: str,
        files: typing.Union[
            str,
            pathlib.Path,
            FilePayload,
            typing.List[typing.Union[str, pathlib.Path]],
            typing.List[FilePayload],
        ],
        *,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.set_input_files

        This method expects `selector` to point to an
        [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

        Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they
        are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        files : Union[List[Union[pathlib.Path, str]], List[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.set_input_files",
                self._impl_obj.set_input_files(
                    selector=selector,
                    files=files,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def type(
        self,
        selector: str,
        text: str,
        *,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.type

        Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `frame.type` can be used to
        send fine-grained keyboard events. To fill values in form fields, use `frame.fill()`.

        To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

        ```py
        await frame.type(\"#mytextarea\", \"hello\") # types instantly
        await frame.type(\"#mytextarea\", \"world\", delay=100) # types slower, like a user
        ```

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.type",
                self._impl_obj.type(
                    selector=selector,
                    text=text,
                    delay=delay,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def press(
        self,
        selector: str,
        key: str,
        *,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.press

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: \"Control+o\"` or `key: \"Control+Shift+T\"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.press",
                self._impl_obj.press(
                    selector=selector,
                    key=key,
                    delay=delay,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def check(
        self,
        selector: str,
        *,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.check

        This method checks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           checked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now checked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.check",
                self._impl_obj.check(
                    selector=selector,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def uncheck(
        self,
        selector: str,
        *,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Frame.uncheck

        This method checks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           unchecked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now unchecked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.uncheck",
                self._impl_obj.uncheck(
                    selector=selector,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def wait_for_timeout(self, timeout: float) -> NoneType:
        """Frame.wait_for_timeout

        Waits for the given `timeout` in milliseconds.

        Note that `frame.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going to
        be flaky. Use signals such as network events, selectors becoming visible and others instead.

        Parameters
        ----------
        timeout : float
            A timeout to wait for
        """

        return mapping.from_maybe_impl(
            await self._async(
                "frame.wait_for_timeout",
                self._impl_obj.wait_for_timeout(timeout=timeout),
            )
        )

    async def wait_for_function(
        self,
        expression: str,
        *,
        arg: typing.Any = None,
        timeout: float = None,
        polling: typing.Union[float, Literal["raf"]] = None
    ) -> "JSHandle":
        """Frame.wait_for_function

        Returns when the `expression` returns a truthy value, returns that value.

        The `frame.wait_for_function()` can be used to observe viewport size change:

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            webkit = playwright.webkit
            browser = await webkit.launch()
            page = await browser.new_page()
            await page.evaluate(\"window.x = 0; setTimeout(() => { window.x = 100 }, 1000);\")
            await page.main_frame.wait_for_function(\"() => window.x > 0\")
            await browser.close()

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        To pass an argument to the predicate of `frame.waitForFunction` function:

        ```py
        selector = \".foo\"
        await frame.wait_for_function(\"selector => !!document.querySelector(selector)\", selector)
        ```

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.
        polling : Union["raf", float, NoneType]
            If `polling` is `'raf'`, then `expression` is constantly executed in `requestAnimationFrame` callback. If `polling` is a
            number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`.

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "frame.wait_for_function",
                self._impl_obj.wait_for_function(
                    expression=expression,
                    arg=mapping.to_impl(arg),
                    timeout=timeout,
                    polling=polling,
                ),
            )
        )

    async def title(self) -> str:
        """Frame.title

        Returns the page title.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("frame.title", self._impl_obj.title())
        )


mapping.register(FrameImpl, Frame)


class Worker(AsyncBase):
    def __init__(self, obj: WorkerImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Worker.url

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    async def evaluate(self, expression: str, arg: typing.Any = None) -> typing.Any:
        """Worker.evaluate

        Returns the return value of `expression`.

        If the function passed to the `worker.evaluate()` returns a [Promise], then `worker.evaluate()` would
        wait for the promise to resolve and return its value.

        If the function passed to the `worker.evaluate()` returns a non-[Serializable] value, then
        `worker.evaluate()` returns `undefined`. Playwright also supports transferring some additional values that are
        not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "worker.evaluate",
                self._impl_obj.evaluate(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def evaluate_handle(
        self, expression: str, arg: typing.Any = None
    ) -> "JSHandle":
        """Worker.evaluate_handle

        Returns the return value of `expression` as a `JSHandle`.

        The only difference between `worker.evaluate()` and `worker.evaluate_handle()` is that
        `worker.evaluate_handle()` returns `JSHandle`.

        If the function passed to the `worker.evaluate_handle()` returns a [Promise], then
        `worker.evaluate_handle()` would wait for the promise to resolve and return its value.

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "worker.evaluate_handle",
                self._impl_obj.evaluate_handle(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )


mapping.register(WorkerImpl, Worker)


class Selectors(AsyncBase):
    def __init__(self, obj: SelectorsImpl):
        super().__init__(obj)

    async def register(
        self,
        name: str,
        script: str = None,
        *,
        path: typing.Union[str, pathlib.Path] = None,
        content_script: bool = None
    ) -> NoneType:
        """Selectors.register

        An example of registering selector engine that queries elements based on a tag name:

        ```py
        # FIXME: add snippet
        ```

        Parameters
        ----------
        name : str
            Name that is used in selectors as a prefix, e.g. `{name: 'foo'}` enables `foo=myselectorbody` selectors. May only
            contain `[a-zA-Z0-9_]` characters.
        script : Union[str, NoneType]
            Raw script content.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working
            directory.
        content_script : Union[bool, NoneType]
            Whether to run this selector engine in isolated JavaScript environment. This environment has access to the same DOM, but
            not any JavaScript objects from the frame's scripts. Defaults to `false`. Note that running as a content script is not
            guaranteed when this engine is used together with other registered engines.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "selectors.register",
                self._impl_obj.register(
                    name=name, script=script, path=path, contentScript=content_script
                ),
            )
        )


mapping.register(SelectorsImpl, Selectors)


class ConsoleMessage(AsyncBase):
    def __init__(self, obj: ConsoleMessageImpl):
        super().__init__(obj)

    @property
    def type(self) -> str:
        """ConsoleMessage.type

        One of the following values: `'log'`, `'debug'`, `'info'`, `'error'`, `'warning'`, `'dir'`, `'dirxml'`, `'table'`,
        `'trace'`, `'clear'`, `'startGroup'`, `'startGroupCollapsed'`, `'endGroup'`, `'assert'`, `'profile'`, `'profileEnd'`,
        `'count'`, `'timeEnd'`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.type)

    @property
    def text(self) -> str:
        """ConsoleMessage.text

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.text)

    @property
    def args(self) -> typing.List["JSHandle"]:
        """ConsoleMessage.args

        Returns
        -------
        List[JSHandle]
        """
        return mapping.from_impl_list(self._impl_obj.args)

    @property
    def location(self) -> SourceLocation:
        """ConsoleMessage.location

        Returns
        -------
        {url: str, lineNumber: int, columnNumber: int}
        """
        return mapping.from_impl(self._impl_obj.location)


mapping.register(ConsoleMessageImpl, ConsoleMessage)


class Dialog(AsyncBase):
    def __init__(self, obj: DialogImpl):
        super().__init__(obj)

    @property
    def type(self) -> str:
        """Dialog.type

        Returns dialog's type, can be one of `alert`, `beforeunload`, `confirm` or `prompt`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.type)

    @property
    def message(self) -> str:
        """Dialog.message

        A message displayed in the dialog.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.message)

    @property
    def default_value(self) -> str:
        """Dialog.default_value

        If dialog is prompt, returns default prompt value. Otherwise, returns empty string.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.default_value)

    async def accept(self, prompt_text: str = None) -> NoneType:
        """Dialog.accept

        Returns when the dialog has been accepted.

        Parameters
        ----------
        prompt_text : Union[str, NoneType]
            A text to enter in prompt. Does not cause any effects if the dialog's `type` is not prompt. Optional.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "dialog.accept", self._impl_obj.accept(promptText=prompt_text)
            )
        )

    async def dismiss(self) -> NoneType:
        """Dialog.dismiss

        Returns when the dialog has been dismissed.
        """

        return mapping.from_maybe_impl(
            await self._async("dialog.dismiss", self._impl_obj.dismiss())
        )


mapping.register(DialogImpl, Dialog)


class Download(AsyncBase):
    def __init__(self, obj: DownloadImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Download.url

        Returns downloaded url.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def suggested_filename(self) -> str:
        """Download.suggested_filename

        Returns suggested filename for this download. It is typically computed by the browser from the
        [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) response header
        or the `download` attribute. See the spec on [whatwg](https://html.spec.whatwg.org/#downloading-resources). Different
        browsers can use different logic for computing it.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.suggested_filename)

    async def delete(self) -> NoneType:
        """Download.delete

        Deletes the downloaded file. Will wait for the download to finish if necessary.
        """

        return mapping.from_maybe_impl(
            await self._async("download.delete", self._impl_obj.delete())
        )

    async def failure(self) -> typing.Optional[str]:
        """Download.failure

        Returns download error if any. Will wait for the download to finish if necessary.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async("download.failure", self._impl_obj.failure())
        )

    async def path(self) -> typing.Optional[pathlib.Path]:
        """Download.path

        Returns path to the downloaded file in case of successful download. The method will wait for the download to finish if
        necessary.

        Returns
        -------
        Union[pathlib.Path, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async("download.path", self._impl_obj.path())
        )

    async def save_as(self, path: typing.Union[str, pathlib.Path]) -> NoneType:
        """Download.save_as

        Saves the download to a user-specified path. It is safe to call this method while the download is still in progress.

        Parameters
        ----------
        path : Union[pathlib.Path, str]
            Path where the download should be saved.
        """

        return mapping.from_maybe_impl(
            await self._async("download.save_as", self._impl_obj.save_as(path=path))
        )


mapping.register(DownloadImpl, Download)


class Video(AsyncBase):
    def __init__(self, obj: VideoImpl):
        super().__init__(obj)

    async def path(self) -> pathlib.Path:
        """Video.path

        Returns the file system path this video will be recorded to. The video is guaranteed to be written to the filesystem
        upon closing the browser context.

        Returns
        -------
        pathlib.Path
        """

        return mapping.from_maybe_impl(
            await self._async("video.path", self._impl_obj.path())
        )


mapping.register(VideoImpl, Video)


class Page(AsyncBase):
    def __init__(self, obj: PageImpl):
        super().__init__(obj)

    @property
    def accessibility(self) -> "Accessibility":
        """Page.accessibility

        Returns
        -------
        Accessibility
        """
        return mapping.from_impl(self._impl_obj.accessibility)

    @property
    def keyboard(self) -> "Keyboard":
        """Page.keyboard

        Returns
        -------
        Keyboard
        """
        return mapping.from_impl(self._impl_obj.keyboard)

    @property
    def mouse(self) -> "Mouse":
        """Page.mouse

        Returns
        -------
        Mouse
        """
        return mapping.from_impl(self._impl_obj.mouse)

    @property
    def touchscreen(self) -> "Touchscreen":
        """Page.touchscreen

        Returns
        -------
        Touchscreen
        """
        return mapping.from_impl(self._impl_obj.touchscreen)

    @property
    def context(self) -> "BrowserContext":
        """Page.context

        Get the browser context that the page belongs to.

        Returns
        -------
        BrowserContext
        """
        return mapping.from_impl(self._impl_obj.context)

    @property
    def main_frame(self) -> "Frame":
        """Page.main_frame

        The page's main frame. Page is guaranteed to have a main frame which persists during navigations.

        Returns
        -------
        Frame
        """
        return mapping.from_impl(self._impl_obj.main_frame)

    @property
    def frames(self) -> typing.List["Frame"]:
        """Page.frames

        An array of all frames attached to the page.

        Returns
        -------
        List[Frame]
        """
        return mapping.from_impl_list(self._impl_obj.frames)

    @property
    def url(self) -> str:
        """Page.url

        Shortcut for main frame's `frame.url()`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def viewport_size(self) -> typing.Optional[ViewportSize]:
        """Page.viewport_size

        Returns
        -------
        Union[{width: int, height: int}, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.viewport_size)

    @property
    def workers(self) -> typing.List["Worker"]:
        """Page.workers

        This method returns all of the dedicated [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)
        associated with the page.

        > NOTE: This does not contain ServiceWorkers

        Returns
        -------
        List[Worker]
        """
        return mapping.from_impl_list(self._impl_obj.workers)

    @property
    def video(self) -> typing.Optional["Video"]:
        """Page.video

        Video object associated with this page.

        Returns
        -------
        Union[Video, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.video)

    async def opener(self) -> typing.Optional["Page"]:
        """Page.opener

        Returns the opener for popup pages and `null` for others. If the opener has been closed already the returns `null`.

        Returns
        -------
        Union[Page, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async("page.opener", self._impl_obj.opener())
        )

    def frame(
        self,
        name: str = None,
        *,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None
    ) -> typing.Optional["Frame"]:
        """Page.frame

        Returns frame matching the specified criteria. Either `name` or `url` must be specified.

        ```py
        frame = page.frame(name=\"frame-name\")
        ```

        ```py
        frame = page.frame(url=r\".*domain.*\")
        ```

        Parameters
        ----------
        name : Union[str, NoneType]
            Frame name specified in the `iframe`'s `name` attribute. Optional.
        url : Union[Callable[[str], bool], Pattern, str, NoneType]
            A glob pattern, regex pattern or predicate receiving frame's `url` as a [URL] object. Optional.

        Returns
        -------
        Union[Frame, NoneType]
        """

        return mapping.from_impl_nullable(
            self._impl_obj.frame(name=name, url=self._wrap_handler(url))
        )

    def set_default_navigation_timeout(self, timeout: float) -> NoneType:
        """Page.set_default_navigation_timeout

        This setting will change the default maximum navigation time for the following methods and related shortcuts:
        - `page.go_back()`
        - `page.go_forward()`
        - `page.goto()`
        - `page.reload()`
        - `page.set_content()`
        - `page.expect_navigation()`

        > NOTE: `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`,
        `browser_context.set_default_timeout()` and `browser_context.set_default_navigation_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum navigation time in milliseconds
        """

        return mapping.from_maybe_impl(
            self._impl_obj.set_default_navigation_timeout(timeout=timeout)
        )

    def set_default_timeout(self, timeout: float) -> NoneType:
        """Page.set_default_timeout

        This setting will change the default maximum time for all the methods accepting `timeout` option.

        > NOTE: `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum time in milliseconds
        """

        return mapping.from_maybe_impl(
            self._impl_obj.set_default_timeout(timeout=timeout)
        )

    async def query_selector(self, selector: str) -> typing.Optional["ElementHandle"]:
        """Page.query_selector

        The method finds an element matching the specified selector within the page. If no elements match the selector, the
        return value resolves to `null`.

        Shortcut for main frame's `frame.query_selector()`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "page.query_selector", self._impl_obj.query_selector(selector=selector)
            )
        )

    async def query_selector_all(self, selector: str) -> typing.List["ElementHandle"]:
        """Page.query_selector_all

        The method finds all elements matching the specified selector within the page. If no elements match the selector, the
        return value resolves to `[]`.

        Shortcut for main frame's `frame.query_selector_all()`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.

        Returns
        -------
        List[ElementHandle]
        """

        return mapping.from_impl_list(
            await self._async(
                "page.query_selector_all",
                self._impl_obj.query_selector_all(selector=selector),
            )
        )

    async def wait_for_selector(
        self,
        selector: str,
        *,
        timeout: float = None,
        state: Literal["attached", "detached", "hidden", "visible"] = None
    ) -> typing.Optional["ElementHandle"]:
        """Page.wait_for_selector

        Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
        `detached`.

        Wait for the `selector` to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If at
        the moment of calling the method `selector` already satisfies the condition, the method will return immediately. If the
        selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

        This method works across navigations:

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            chromium = playwright.chromium
            browser = await chromium.launch()
            page = await browser.new_page()
            for current_url in [\"https://google.com\", \"https://bbc.com\"]:
                await page.goto(current_url, wait_until=\"domcontentloaded\")
                element = await page.wait_for_selector(\"img\")
                print(\"Loaded image: \" + str(await element.get_attribute(\"src\")))
            await browser.close()

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        state : Union["attached", "detached", "hidden", "visible", NoneType]
            Defaults to `'visible'`. Can be either:
            - `'attached'` - wait for element to be present in DOM.
            - `'detached'` - wait for element to not be present in DOM.
            - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without
              any content or with `display:none` has an empty bounding box and is not considered visible.
            - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`.
              This is opposite to the `'visible'` option.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "page.wait_for_selector",
                self._impl_obj.wait_for_selector(
                    selector=selector, timeout=timeout, state=state
                ),
            )
        )

    async def is_checked(self, selector: str, *, timeout: float = None) -> bool:
        """Page.is_checked

        Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.is_checked",
                self._impl_obj.is_checked(selector=selector, timeout=timeout),
            )
        )

    async def is_disabled(self, selector: str, *, timeout: float = None) -> bool:
        """Page.is_disabled

        Returns whether the element is disabled, the opposite of [enabled](./actionability.md#enabled).

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.is_disabled",
                self._impl_obj.is_disabled(selector=selector, timeout=timeout),
            )
        )

    async def is_editable(self, selector: str, *, timeout: float = None) -> bool:
        """Page.is_editable

        Returns whether the element is [editable](./actionability.md#editable).

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.is_editable",
                self._impl_obj.is_editable(selector=selector, timeout=timeout),
            )
        )

    async def is_enabled(self, selector: str, *, timeout: float = None) -> bool:
        """Page.is_enabled

        Returns whether the element is [enabled](./actionability.md#enabled).

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.is_enabled",
                self._impl_obj.is_enabled(selector=selector, timeout=timeout),
            )
        )

    async def is_hidden(self, selector: str, *, timeout: float = None) -> bool:
        """Page.is_hidden

        Returns whether the element is hidden, the opposite of [visible](./actionability.md#visible).  `selector` that does not
        match any elements is considered hidden.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.is_hidden",
                self._impl_obj.is_hidden(selector=selector, timeout=timeout),
            )
        )

    async def is_visible(self, selector: str, *, timeout: float = None) -> bool:
        """Page.is_visible

        Returns whether the element is [visible](./actionability.md#visible). `selector` that does not match any elements is
        considered not visible.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.is_visible",
                self._impl_obj.is_visible(selector=selector, timeout=timeout),
            )
        )

    async def dispatch_event(
        self,
        selector: str,
        type: str,
        event_init: typing.Dict = None,
        *,
        timeout: float = None
    ) -> NoneType:
        """Page.dispatch_event

        The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the elment, `click`
        is dispatched. This is equivalend to calling
        [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

        ```py
        await page.dispatch_event(\"button#submit\", \"click\")
        ```

        Under the hood, it creates an instance of an event based on the given `type`, initializes it with `eventInit` properties
        and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

        Since `eventInit` is event-specific, please refer to the events documentation for the lists of initial properties:
        - [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
        - [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
        - [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
        - [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
        - [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
        - [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
        - [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

        You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

        ```py
        # note you can only create data_transfer in chromium and firefox
        data_transfer = await page.evaluate_handle(\"new DataTransfer()\")
        await page.dispatch_event(\"#source\", \"dragstart\", { \"dataTransfer\": data_transfer })
        ```

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        type : str
            DOM event type: `"click"`, `"dragstart"`, etc.
        event_init : Union[Dict, NoneType]
            Optional event-specific initialization properties.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.dispatch_event",
                self._impl_obj.dispatch_event(
                    selector=selector,
                    type=type,
                    eventInit=mapping.to_impl(event_init),
                    timeout=timeout,
                ),
            )
        )

    async def evaluate(self, expression: str, arg: typing.Any = None) -> typing.Any:
        """Page.evaluate

        Returns the value of the `expression` invocation.

        If the function passed to the `page.evaluate()` returns a [Promise], then `page.evaluate()` would wait
        for the promise to resolve and return its value.

        If the function passed to the `page.evaluate()` returns a non-[Serializable] value, then
        `page.evaluate()` resolves to `undefined`. Playwright also supports transferring some additional values that are
        not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

        Passing argument to `expression`:

        ```py
        result = await page.evaluate(\"([x, y]) => Promise.resolve(x * y)\", [7, 8])
        print(result) # prints \"56\"
        ```

        A string can also be passed in instead of a function:

        ```py
        print(await page.evaluate(\"1 + 2\")) # prints \"3\"
        x = 10
        print(await page.evaluate(f\"1 + {x}\")) # prints \"11\"
        ```

        `ElementHandle` instances can be passed as an argument to the `page.evaluate()`:

        ```py
        body_handle = await page.query_selector(\"body\")
        html = await page.evaluate(\"([body, suffix]) => body.innerHTML + suffix\", [body_handle, \"hello\"])
        await body_handle.dispose()
        ```

        Shortcut for main frame's `frame.evaluate()`.

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.evaluate",
                self._impl_obj.evaluate(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def evaluate_handle(
        self, expression: str, arg: typing.Any = None
    ) -> "JSHandle":
        """Page.evaluate_handle

        Returns the value of the `expression` invocation as a `JSHandle`.

        The only difference between `page.evaluate()` and `page.evaluate_handle()` is that
        `page.evaluate_handle()` returns `JSHandle`.

        If the function passed to the `page.evaluate_handle()` returns a [Promise], then `page.evaluate_handle()`
        would wait for the promise to resolve and return its value.

        ```py
        a_window_handle = await page.evaluate_handle(\"Promise.resolve(window)\")
        a_window_handle # handle for the window object.
        ```

        A string can also be passed in instead of a function:

        ```py
        a_handle = await page.evaluate_handle(\"document\") # handle for the \"document\"
        ```

        `JSHandle` instances can be passed as an argument to the `page.evaluate_handle()`:

        ```py
        a_handle = await page.evaluate_handle(\"document.body\")
        result_handle = await page.evaluate_handle(\"body => body.innerHTML\", a_handle)
        print(await result_handle.json_value())
        await result_handle.dispose()
        ```

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "page.evaluate_handle",
                self._impl_obj.evaluate_handle(
                    expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def eval_on_selector(
        self, selector: str, expression: str, arg: typing.Any = None
    ) -> typing.Any:
        """Page.eval_on_selector

        The method finds an element matching the specified selector within the page and passes it as a first argument to
        `expression`. If no elements match the selector, the method throws an error. Returns the value of `expression`.

        If `expression` returns a [Promise], then `page.eval_on_selector()` would wait for the promise to resolve and
        return its value.

        Examples:

        ```py
        search_value = await page.eval_on_selector(\"#search\", \"el => el.value\")
        preload_href = await page.eval_on_selector(\"link[rel=preload]\", \"el => el.href\")
        html = await page.eval_on_selector(\".main-container\", \"(e, suffix) => e.outer_html + suffix\", \"hello\")
        ```

        Shortcut for main frame's `frame.eval_on_selector()`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.eval_on_selector",
                self._impl_obj.eval_on_selector(
                    selector=selector, expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def eval_on_selector_all(
        self, selector: str, expression: str, arg: typing.Any = None
    ) -> typing.Any:
        """Page.eval_on_selector_all

        The method finds all elements matching the specified selector within the page and passes an array of matched elements as
        a first argument to `expression`. Returns the result of `expression` invocation.

        If `expression` returns a [Promise], then `page.eval_on_selector_all()` would wait for the promise to resolve and
        return its value.

        Examples:

        ```py
        div_counts = await page.eval_on_selector_all(\"div\", \"(divs, min) => divs.length >= min\", 10)
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md) for more details.
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.eval_on_selector_all",
                self._impl_obj.eval_on_selector_all(
                    selector=selector, expression=expression, arg=mapping.to_impl(arg)
                ),
            )
        )

    async def add_script_tag(
        self,
        *,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None,
        type: str = None
    ) -> "ElementHandle":
        """Page.add_script_tag

        Adds a `<script>` tag into the page with the desired url or content. Returns the added tag when the script's onload
        fires or when the script content was injected into frame.

        Shortcut for main frame's `frame.add_script_tag()`.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of a script to be added.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory.
        content : Union[str, NoneType]
            Raw JavaScript content to be injected into frame.
        type : Union[str, NoneType]
            Script type. Use 'module' in order to load a Javascript ES6 module. See
            [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details.

        Returns
        -------
        ElementHandle
        """

        return mapping.from_impl(
            await self._async(
                "page.add_script_tag",
                self._impl_obj.add_script_tag(
                    url=url, path=path, content=content, type=type
                ),
            )
        )

    async def add_style_tag(
        self,
        *,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None
    ) -> "ElementHandle":
        """Page.add_style_tag

        Adds a `<link rel=\"stylesheet\">` tag into the page with the desired url or a `<style type=\"text/css\">` tag with the
        content. Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

        Shortcut for main frame's `frame.add_style_tag()`.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of the `<link>` tag.
        path : Union[pathlib.Path, str, NoneType]
            Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory.
        content : Union[str, NoneType]
            Raw CSS content to be injected into frame.

        Returns
        -------
        ElementHandle
        """

        return mapping.from_impl(
            await self._async(
                "page.add_style_tag",
                self._impl_obj.add_style_tag(url=url, path=path, content=content),
            )
        )

    async def expose_function(self, name: str, callback: typing.Callable) -> NoneType:
        """Page.expose_function

        The method adds a function called `name` on the `window` object of every frame in the page. When called, the function
        executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

        If the `callback` returns a [Promise], it will be awaited.

        See `browser_context.expose_function()` for context-wide exposed function.

        > NOTE: Functions installed via `page.expose_function()` survive navigations.

        An example of adding an `sha1` function to the page:

        ```py
        import asyncio
        import hashlib
        from playwright.async_api import async_playwright

        async def sha1(text):
            m = hashlib.sha1()
            m.update(bytes(text, \"utf8\"))
            return m.hexdigest()

        async def run(playwright):
            webkit = playwright.webkit
            browser = await webkit.launch(headless=False)
            page = await browser.new_page()
            await page.expose_function(\"sha1\", sha1)
            await page.set_content(\"\"\"
                <script>
                  async function onClick() {
                    document.querySelector('div').textContent = await window.sha1('PLAYWRIGHT');
                  }
                </script>
                <button onclick=\"onClick()\">Click me</button>
                <div></div>
            \"\"\")
            await page.click(\"button\")

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        Parameters
        ----------
        name : str
            Name of the function on the window object
        callback : Callable
            Callback function which will be called in Playwright's context.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.expose_function",
                self._impl_obj.expose_function(
                    name=name, callback=self._wrap_handler(callback)
                ),
            )
        )

    async def expose_binding(
        self, name: str, callback: typing.Callable, *, handle: bool = None
    ) -> NoneType:
        """Page.expose_binding

        The method adds a function called `name` on the `window` object of every frame in this page. When called, the function
        executes `callback` and returns a [Promise] which resolves to the return value of `callback`. If the `callback` returns
        a [Promise], it will be awaited.

        The first argument of the `callback` function contains information about the caller: `{ browserContext: BrowserContext,
        page: Page, frame: Frame }`.

        See `browser_context.expose_binding()` for the context-wide version.

        > NOTE: Functions installed via `page.expose_binding()` survive navigations.

        An example of exposing page URL to all frames in a page:

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            webkit = playwright.webkit
            browser = await webkit.launch(headless=false)
            context = await browser.new_context()
            page = await context.new_page()
            await page.expose_binding(\"pageURL\", lambda source: source[\"page\"].url)
            await page.set_content(\"\"\"
            <script>
              async function onClick() {
                document.querySelector('div').textContent = await window.pageURL();
              }
            </script>
            <button onclick=\"onClick()\">Click me</button>
            <div></div>
            \"\"\")
            await page.click(\"button\")

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        An example of passing an element handle:

        ```py
        async def print(source, element):
            print(await element.text_content())

        await page.expose_binding(\"clicked\", print, handle=true)
        await page.set_content(\"\"\"
          <script>
            document.addEventListener('click', event => window.clicked(event.target));
          </script>
          <div>Click me</div>
          <div>Or click me</div>
        \"\"\")
        ```

        Parameters
        ----------
        name : str
            Name of the function on the window object.
        callback : Callable
            Callback function that will be called in the Playwright's context.
        handle : Union[bool, NoneType]
            Whether to pass the argument as a handle, instead of passing by value. When passing a handle, only one argument is
            supported. When passing by value, multiple arguments are supported.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.expose_binding",
                self._impl_obj.expose_binding(
                    name=name, callback=self._wrap_handler(callback), handle=handle
                ),
            )
        )

    async def set_extra_http_headers(self, headers: typing.Dict[str, str]) -> NoneType:
        """Page.set_extra_http_headers

        The extra HTTP headers will be sent with every request the page initiates.

        > NOTE: `page.set_extra_http_headers()` does not guarantee the order of headers in the outgoing requests.

        Parameters
        ----------
        headers : Dict[str, str]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.set_extra_http_headers",
                self._impl_obj.set_extra_http_headers(headers=mapping.to_impl(headers)),
            )
        )

    async def content(self) -> str:
        """Page.content

        Gets the full HTML contents of the page, including the doctype.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("page.content", self._impl_obj.content())
        )

    async def set_content(
        self,
        html: str,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None
    ) -> NoneType:
        """Page.set_content

        Parameters
        ----------
        html : str
            HTML markup to assign to the page.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.set_content",
                self._impl_obj.set_content(
                    html=html, timeout=timeout, waitUntil=wait_until
                ),
            )
        )

    async def goto(
        self,
        url: str,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        referer: str = None
    ) -> typing.Optional["Response"]:
        """Page.goto

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect.

        `page.goto` will throw an error if:
        - there's an SSL error (e.g. in case of self-signed certificates).
        - target URL is invalid.
        - the `timeout` is exceeded during navigation.
        - the remote server does not respond or is unreachable.
        - the main resource failed to load.

        `page.goto` will not throw an error when any valid HTTP status code is returned by the remote server, including 404 \"Not
        Found\" and 500 \"Internal Server Error\".  The status code for such responses can be retrieved by calling
        `response.status()`.

        > NOTE: `page.goto` either throws an error or returns a main resource response. The only exceptions are navigation to
        `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.
        > NOTE: Headless mode doesn't support navigation to a PDF document. See the
        [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

        Shortcut for main frame's `frame.goto()`

        Parameters
        ----------
        url : str
            URL to navigate page to. The url should include scheme, e.g. `https://`.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        referer : Union[str, NoneType]
            Referer header value. If provided it will take preference over the referer header value set by
            `page.set_extra_http_headers()`.

        Returns
        -------
        Union[Response, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "page.goto",
                self._impl_obj.goto(
                    url=url, timeout=timeout, waitUntil=wait_until, referer=referer
                ),
            )
        )

    async def reload(
        self,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None
    ) -> typing.Optional["Response"]:
        """Page.reload

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

        Returns
        -------
        Union[Response, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "page.reload",
                self._impl_obj.reload(timeout=timeout, waitUntil=wait_until),
            )
        )

    async def wait_for_load_state(
        self,
        state: Literal["domcontentloaded", "load", "networkidle"] = None,
        *,
        timeout: float = None
    ) -> NoneType:
        """Page.wait_for_load_state

        Returns when the required load state has been reached.

        This resolves when the page reaches a required load state, `load` by default. The navigation must have been committed
        when this method is called. If current document has already reached the required state, resolves immediately.

        ```py
        await page.click(\"button\") # click triggers navigation.
        await page.wait_for_load_state() # the promise resolves after \"load\" event.
        ```

        ```py
        async with page.expect_popup() as page_info:
            await page.click(\"button\") # click triggers a popup.
        popup = await page_info.value
         # Following resolves after \"domcontentloaded\" event.
        await popup.wait_for_load_state(\"domcontentloaded\")
        print(await popup.title()) # popup is ready to use.
        ```

        Shortcut for main frame's `frame.wait_for_load_state()`.

        Parameters
        ----------
        state : Union["domcontentloaded", "load", "networkidle", NoneType]
            Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current
            document, the method resolves immediately. Can be one of:
            - `'load'` - wait for the `load` event to be fired.
            - `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired.
            - `'networkidle'` - wait until there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.wait_for_load_state",
                self._impl_obj.wait_for_load_state(state=state, timeout=timeout),
            )
        )

    async def wait_for_event(
        self, event: str, predicate: typing.Callable = None, *, timeout: float = None
    ) -> typing.Any:
        """Page.wait_for_event

        > NOTE: In most cases, you should use `page.expect_event()`.

        Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function and
        waits for `predicate(event)` to return a truthy value. Will throw an error if the socket is closed before the `event` is
        fired.

        Parameters
        ----------
        event : str
            Event name, same one typically passed into `*.on(event)`.
        predicate : Union[Callable, NoneType]
            Receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.wait_for_event",
                self._impl_obj.wait_for_event(
                    event=event,
                    predicate=self._wrap_handler(predicate),
                    timeout=timeout,
                ),
            )
        )

    async def go_back(
        self,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None
    ) -> typing.Optional["Response"]:
        """Page.go_back

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect. If can not go back, returns `null`.

        Navigate to the previous page in history.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

        Returns
        -------
        Union[Response, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "page.go_back",
                self._impl_obj.go_back(timeout=timeout, waitUntil=wait_until),
            )
        )

    async def go_forward(
        self,
        *,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None
    ) -> typing.Optional["Response"]:
        """Page.go_forward

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect. If can not go forward, returns `null`.

        Navigate to the next page in history.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

        Returns
        -------
        Union[Response, NoneType]
        """

        return mapping.from_impl_nullable(
            await self._async(
                "page.go_forward",
                self._impl_obj.go_forward(timeout=timeout, waitUntil=wait_until),
            )
        )

    async def emulate_media(
        self,
        *,
        media: Literal["print", "screen"] = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None
    ) -> NoneType:
        """Page.emulate_media

        ```py
        await page.evaluate(\"matchMedia('screen').matches\")
        # → True
        await page.evaluate(\"matchMedia('print').matches\")
        # → False

        await page.emulate_media(media=\"print\")
        await page.evaluate(\"matchMedia('screen').matches\")
        # → False
        await page.evaluate(\"matchMedia('print').matches\")
        # → True

        await page.emulate_media()
        await page.evaluate(\"matchMedia('screen').matches\")
        # → True
        await page.evaluate(\"matchMedia('print').matches\")
        # → False
        ```

        ```py
        await page.emulate_media(color_scheme=\"dark\")
        await page.evaluate(\"matchMedia('(prefers-color-scheme: dark)').matches\")
        # → True
        await page.evaluate(\"matchMedia('(prefers-color-scheme: light)').matches\")
        # → False
        await page.evaluate(\"matchMedia('(prefers-color-scheme: no-preference)').matches\")
        # → False
        ```

        Parameters
        ----------
        media : Union["print", "screen", NoneType]
            Changes the CSS media type of the page. The only allowed values are `'screen'`, `'print'` and `null`. Passing `null`
            disables CSS media emulation.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. Passing
            `null` disables color scheme emulation.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.emulate_media",
                self._impl_obj.emulate_media(media=media, colorScheme=color_scheme),
            )
        )

    async def set_viewport_size(self, viewport_size: ViewportSize) -> NoneType:
        """Page.set_viewport_size

        In the case of multiple pages in a single browser, each page can have its own viewport size. However,
        `browser.new_context()` allows to set viewport size (and more) for all pages in the context at once.

        `page.setViewportSize` will resize the page. A lot of websites don't expect phones to change size, so you should set the
        viewport size before navigating to the page.

        ```py
        page = await browser.new_page()
        await page.set_viewport_size({\"width\": 640, \"height\": 480})
        await page.goto(\"https://example.com\")
        ```

        Parameters
        ----------
        viewport_size : {width: int, height: int}
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.set_viewport_size",
                self._impl_obj.set_viewport_size(viewportSize=viewport_size),
            )
        )

    async def bring_to_front(self) -> NoneType:
        """Page.bring_to_front

        Brings page to front (activates tab).
        """

        return mapping.from_maybe_impl(
            await self._async("page.bring_to_front", self._impl_obj.bring_to_front())
        )

    async def add_init_script(
        self, script: str = None, *, path: typing.Union[str, pathlib.Path] = None
    ) -> NoneType:
        """Page.add_init_script

        Adds a script which would be evaluated in one of the following scenarios:
        - Whenever the page is navigated.
        - Whenever the child frame is attached or navigated. In this case, the script is evaluated in the context of the newly
          attached frame.

        The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend
        the JavaScript environment, e.g. to seed `Math.random`.

        An example of overriding `Math.random` before the page loads:

        ```py
        # in your playwright script, assuming the preload.js file is in same directory
        await page.add_init_script(path=\"./preload.js\")
        ```

        > NOTE: The order of evaluation of multiple scripts installed via `browser_context.add_init_script()` and
        `page.add_init_script()` is not defined.

        Parameters
        ----------
        script : Union[str, NoneType]
            Script to be evaluated in all pages in the browser context. Optional.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working
            directory. Optional.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.add_init_script",
                self._impl_obj.add_init_script(script=script, path=path),
            )
        )

    async def route(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ],
    ) -> NoneType:
        """Page.route

        Routing provides the capability to modify network requests that are made by a page.

        Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

        > NOTE: The handler will only be called for the first url if the response is a redirect.

        An example of a naïve handler that aborts all image requests:

        ```py
        page = await browser.new_page()
        await page.route(\"**/*.{png,jpg,jpeg}\", lambda route: route.abort())
        await page.goto(\"https://example.com\")
        await browser.close()
        ```

        or the same snippet using a regex pattern instead:

        ```py
        page = await browser.new_page()
        await page.route(re.compile(r\"(\\.png$)|(\\.jpg$)\"), lambda route: route.abort())
        await page.goto(\"https://example.com\")
        await browser.close()
        ```

        Page routes take precedence over browser context routes (set up with `browser_context.route()`) when request
        matches both handlers.

        > NOTE: Enabling routing disables http cache.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] to match while routing.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any]]
            handler function to route the request.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.route",
                self._impl_obj.route(
                    url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                ),
            )
        )

    async def unroute(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ] = None,
    ) -> NoneType:
        """Page.unroute

        Removes a route created with `page.route()`. When `handler` is not specified, removes all routes for the `url`.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] to match while routing.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any], NoneType]
            Optional handler function to route the request.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.unroute",
                self._impl_obj.unroute(
                    url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                ),
            )
        )

    async def screenshot(
        self,
        *,
        timeout: float = None,
        type: Literal["jpeg", "png"] = None,
        path: typing.Union[str, pathlib.Path] = None,
        quality: int = None,
        omit_background: bool = None,
        full_page: bool = None,
        clip: FloatRect = None
    ) -> bytes:
        """Page.screenshot

        Returns the buffer with the captured screenshot.

        > NOTE: Screenshots take at least 1/6 second on Chromium OS X and Chromium Windows. See https://crbug.com/741689 for
        discussion.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        type : Union["jpeg", "png", NoneType]
            Specify screenshot type, defaults to `png`.
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the image to. The screenshot type will be inferred from file extension. If `path` is a relative
            path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to
            the disk.
        quality : Union[int, NoneType]
            The quality of the image, between 0-100. Not applicable to `png` images.
        omit_background : Union[bool, NoneType]
            Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images.
            Defaults to `false`.
        full_page : Union[bool, NoneType]
            When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Defaults to
            `false`.
        clip : Union[{x: float, y: float, width: float, height: float}, NoneType]
            An object which specifies clipping of the resulting image. Should have the following fields:

        Returns
        -------
        bytes
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.screenshot",
                self._impl_obj.screenshot(
                    timeout=timeout,
                    type=type,
                    path=path,
                    quality=quality,
                    omitBackground=omit_background,
                    fullPage=full_page,
                    clip=clip,
                ),
            )
        )

    async def title(self) -> str:
        """Page.title

        Returns the page's title. Shortcut for main frame's `frame.title()`.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async("page.title", self._impl_obj.title())
        )

    async def close(self, *, run_before_unload: bool = None) -> NoneType:
        """Page.close

        If `runBeforeUnload` is `false`, does not run any unload handlers and waits for the page to be closed. If
        `runBeforeUnload` is `true` the method will run unload handlers, but will **not** wait for the page to close.

        By default, `page.close()` **does not** run `beforeunload` handlers.

        > NOTE: if `runBeforeUnload` is passed as true, a `beforeunload` dialog might be summoned and should be handled manually
        via `page.on('dialog')` event.

        Parameters
        ----------
        run_before_unload : Union[bool, NoneType]
            Defaults to `false`. Whether to run the
            [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) page handlers.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.close", self._impl_obj.close(runBeforeUnload=run_before_unload)
            )
        )

    def is_closed(self) -> bool:
        """Page.is_closed

        Indicates that the page has been closed.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(self._impl_obj.is_closed())

    async def click(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.click

        This method clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.click()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.click",
                self._impl_obj.click(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    delay=delay,
                    button=button,
                    clickCount=click_count,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def dblclick(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.dblclick

        This method double clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to double click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set. Note that if the
           first click of the `dblclick()` triggers a navigation event, this method will reject.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > NOTE: `page.dblclick()` dispatches two `click` events and a single `dblclick` event.

        Shortcut for main frame's `frame.dblclick()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.dblclick",
                self._impl_obj.dblclick(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    delay=delay,
                    button=button,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def tap(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.tap

        This method taps an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > NOTE: `page.tap()` requires that the `hasTouch` option of the browser context be set to true.

        Shortcut for main frame's `frame.tap()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.tap",
                self._impl_obj.tap(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def fill(
        self,
        selector: str,
        value: str,
        *,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.fill

        This method waits for an element matching `selector`, waits for [actionability](./actionability.md) checks, focuses the
        element, fills it and triggers an `input` event after filling. If the element is inside the `<label>` element that has
        associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), that control will be
        filled instead. If the element to be filled is not an `<input>`, `<textarea>` or `[contenteditable]` element, this
        method throws an error. Note that you can pass an empty string to clear the input field.

        To send fine-grained keyboard events, use `page.type()`.

        Shortcut for main frame's `frame.fill()`

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        value : str
            Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.fill",
                self._impl_obj.fill(
                    selector=selector,
                    value=value,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def focus(self, selector: str, *, timeout: float = None) -> NoneType:
        """Page.focus

        This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the method
        waits until a matching element appears in the DOM.

        Shortcut for main frame's `frame.focus()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.focus", self._impl_obj.focus(selector=selector, timeout=timeout)
            )
        )

    async def text_content(
        self, selector: str, *, timeout: float = None
    ) -> typing.Optional[str]:
        """Page.text_content

        Returns `element.textContent`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.text_content",
                self._impl_obj.text_content(selector=selector, timeout=timeout),
            )
        )

    async def inner_text(self, selector: str, *, timeout: float = None) -> str:
        """Page.inner_text

        Returns `element.innerText`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.inner_text",
                self._impl_obj.inner_text(selector=selector, timeout=timeout),
            )
        )

    async def inner_html(self, selector: str, *, timeout: float = None) -> str:
        """Page.inner_html

        Returns `element.innerHTML`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.inner_html",
                self._impl_obj.inner_html(selector=selector, timeout=timeout),
            )
        )

    async def get_attribute(
        self, selector: str, name: str, *, timeout: float = None
    ) -> typing.Optional[str]:
        """Page.get_attribute

        Returns element attribute value.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        name : str
            Attribute name to get the value for.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.get_attribute",
                self._impl_obj.get_attribute(
                    selector=selector, name=name, timeout=timeout
                ),
            )
        )

    async def hover(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: Position = None,
        timeout: float = None,
        force: bool = None
    ) -> NoneType:
        """Page.hover

        This method hovers over an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to hover over the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.hover()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[{x: float, y: float}, NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.hover",
                self._impl_obj.hover(
                    selector=selector,
                    modifiers=modifiers,
                    position=position,
                    timeout=timeout,
                    force=force,
                ),
            )
        )

    async def select_option(
        self,
        selector: str,
        value: typing.Union[str, typing.List[str]] = None,
        *,
        index: typing.Union[int, typing.List[int]] = None,
        label: typing.Union[str, typing.List[str]] = None,
        element: typing.Union["ElementHandle", typing.List["ElementHandle"]] = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> typing.List[str]:
        """Page.select_option

        Returns the array of option values that have been successfully selected.

        Triggers a `change` and `input` event once all the provided options have been selected. If there's no `<select>` element
        matching `selector`, the method throws an error.

        Will wait until all specified options are present in the `<select>` element.

        ```py
        # single selection matching the value
        await page.select_option(\"select#colors\", \"blue\")
        # single selection matching the label
        await page.select_option(\"select#colors\", label=\"blue\")
        # multiple selection
        await page.select_option(\"select#colors\", value=[\"red\", \"green\", \"blue\"])
        ```

        Shortcut for main frame's `frame.select_option()`

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        value : Union[List[str], str, NoneType]
            Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise
            only the first option matching one of the passed options is selected. Optional.
        index : Union[List[int], int, NoneType]
            Options to select by index. Optional.
        label : Union[List[str], str, NoneType]
            Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise
            only the first option matching one of the passed options is selected. Optional.
        element : Union[ElementHandle, List[ElementHandle], NoneType]
            Option elements to select. Optional.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.

        Returns
        -------
        List[str]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.select_option",
                self._impl_obj.select_option(
                    selector=selector,
                    value=value,
                    index=index,
                    label=label,
                    element=mapping.to_impl(element),
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def set_input_files(
        self,
        selector: str,
        files: typing.Union[
            str,
            pathlib.Path,
            FilePayload,
            typing.List[typing.Union[str, pathlib.Path]],
            typing.List[FilePayload],
        ],
        *,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.set_input_files

        This method expects `selector` to point to an
        [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

        Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they
        are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        files : Union[List[Union[pathlib.Path, str]], List[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.set_input_files",
                self._impl_obj.set_input_files(
                    selector=selector,
                    files=files,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def type(
        self,
        selector: str,
        text: str,
        *,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.type

        Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `page.type` can be used to send
        fine-grained keyboard events. To fill values in form fields, use `page.fill()`.

        To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

        ```py
        await page.type(\"#mytextarea\", \"hello\") # types instantly
        await page.type(\"#mytextarea\", \"world\", delay=100) # types slower, like a user
        ```

        Shortcut for main frame's `frame.type()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.type",
                self._impl_obj.type(
                    selector=selector,
                    text=text,
                    delay=delay,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def press(
        self,
        selector: str,
        key: str,
        *,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.press

        Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: \"Control+o\"` or `key: \"Control+Shift+T\"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        ```py
        page = await browser.new_page()
        await page.goto(\"https://keycode.info\")
        await page.press(\"body\", \"A\")
        await page.screenshot(path=\"a.png\")
        await page.press(\"body\", \"ArrowLeft\")
        await page.screenshot(path=\"arrow_left.png\")
        await page.press(\"body\", \"Shift+O\")
        await page.screenshot(path=\"o.png\")
        await browser.close()
        ```

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.press",
                self._impl_obj.press(
                    selector=selector,
                    key=key,
                    delay=delay,
                    timeout=timeout,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def check(
        self,
        selector: str,
        *,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.check

        This method checks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           checked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now checked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.check()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.check",
                self._impl_obj.check(
                    selector=selector,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def uncheck(
        self,
        selector: str,
        *,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None
    ) -> NoneType:
        """Page.uncheck

        This method unchecks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           unchecked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now unchecked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.uncheck()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.uncheck",
                self._impl_obj.uncheck(
                    selector=selector,
                    timeout=timeout,
                    force=force,
                    noWaitAfter=no_wait_after,
                ),
            )
        )

    async def wait_for_timeout(self, timeout: float) -> NoneType:
        """Page.wait_for_timeout

        Waits for the given `timeout` in milliseconds.

        Note that `page.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going to be
        flaky. Use signals such as network events, selectors becoming visible and others instead.

        ```py
        # wait for 1 second
        await page.wait_for_timeout(1000)
        ```

        Shortcut for main frame's `frame.wait_for_timeout()`.

        Parameters
        ----------
        timeout : float
            A timeout to wait for
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.wait_for_timeout",
                self._impl_obj.wait_for_timeout(timeout=timeout),
            )
        )

    async def wait_for_function(
        self,
        expression: str,
        *,
        arg: typing.Any = None,
        timeout: float = None,
        polling: typing.Union[float, Literal["raf"]] = None
    ) -> "JSHandle":
        """Page.wait_for_function

        Returns when the `expression` returns a truthy value. It resolves to a JSHandle of the truthy value.

        The `page.wait_for_function()` can be used to observe viewport size change:

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            webkit = playwright.webkit
            browser = await webkit.launch()
            page = await browser.new_page()
            await page.evaluate(\"window.x = 0; setTimeout(() => { window.x = 100 }, 1000);\")
            await page.wait_for_function(\"() => window.x > 0\")
            await browser.close()

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        To pass an argument to the predicate of `page.wait_for_function()` function:

        ```py
        selector = \".foo\"
        await page.wait_for_function(\"selector => !!document.querySelector(selector)\", selector)
        ```

        Shortcut for main frame's `frame.wait_for_function()`.

        Parameters
        ----------
        expression : str
            JavaScript expression to be evaluated in the browser context. If it looks like a function declaration, it is interpreted
            as a function. Otherwise, evaluated as an expression.
        arg : Union[Any, NoneType]
            Optional argument to pass to `expression`.
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.
        polling : Union["raf", float, NoneType]
            If `polling` is `'raf'`, then `expression` is constantly executed in `requestAnimationFrame` callback. If `polling` is a
            number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`.

        Returns
        -------
        JSHandle
        """

        return mapping.from_impl(
            await self._async(
                "page.wait_for_function",
                self._impl_obj.wait_for_function(
                    expression=expression,
                    arg=mapping.to_impl(arg),
                    timeout=timeout,
                    polling=polling,
                ),
            )
        )

    async def pause(self) -> NoneType:
        """Page.pause

        Pauses script execution. Playwright will stop executing the script and wait for the user to either press 'Resume' button
        in the page overlay or to call `playwright.resume()` in the DevTools console.

        User can inspect selectors or perform manual steps while paused. Resume will continue running the original script from
        the place it was paused.

        > NOTE: This method requires Playwright to be started in a headed mode, with a falsy `headless` value in the
        `browser_type.launch()`.
        """

        return mapping.from_maybe_impl(
            await self._async("page.pause", self._impl_obj.pause())
        )

    async def pdf(
        self,
        *,
        scale: float = None,
        display_header_footer: bool = None,
        header_template: str = None,
        footer_template: str = None,
        print_background: bool = None,
        landscape: bool = None,
        page_ranges: str = None,
        format: str = None,
        width: typing.Union[str, float] = None,
        height: typing.Union[str, float] = None,
        prefer_css_page_size: bool = None,
        margin: PdfMargins = None,
        path: typing.Union[str, pathlib.Path] = None
    ) -> bytes:
        """Page.pdf

        Returns the PDF buffer.

        > NOTE: Generating a pdf is currently only supported in Chromium headless.

        `page.pdf()` generates a pdf of the page with `print` css media. To generate a pdf with `screen` media, call
        `page.emulate_media()` before calling `page.pdf()`:

        > NOTE: By default, `page.pdf()` generates a pdf with modified colors for printing. Use the
        [`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust) property to
        force rendering of exact colors.

        ```py
        # generates a pdf with \"screen\" media type.
        await page.emulate_media(media=\"screen\")
        await page.pdf(path=\"page.pdf\")
        ```

        The `width`, `height`, and `margin` options accept values labeled with units. Unlabeled values are treated as pixels.

        A few examples:
        - `page.pdf({width: 100})` - prints with width set to 100 pixels
        - `page.pdf({width: '100px'})` - prints with width set to 100 pixels
        - `page.pdf({width: '10cm'})` - prints with width set to 10 centimeters.

        All possible units are:
        - `px` - pixel
        - `in` - inch
        - `cm` - centimeter
        - `mm` - millimeter

        The `format` options are:
        - `Letter`: 8.5in x 11in
        - `Legal`: 8.5in x 14in
        - `Tabloid`: 11in x 17in
        - `Ledger`: 17in x 11in
        - `A0`: 33.1in x 46.8in
        - `A1`: 23.4in x 33.1in
        - `A2`: 16.54in x 23.4in
        - `A3`: 11.7in x 16.54in
        - `A4`: 8.27in x 11.7in
        - `A5`: 5.83in x 8.27in
        - `A6`: 4.13in x 5.83in

        > NOTE: `headerTemplate` and `footerTemplate` markup have the following limitations: > 1. Script tags inside templates
        are not evaluated. > 2. Page styles are not visible inside templates.

        Parameters
        ----------
        scale : Union[float, NoneType]
            Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.
        display_header_footer : Union[bool, NoneType]
            Display header and footer. Defaults to `false`.
        header_template : Union[str, NoneType]
            HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values
            into them:
            - `'date'` formatted print date
            - `'title'` document title
            - `'url'` document location
            - `'pageNumber'` current page number
            - `'totalPages'` total pages in the document
        footer_template : Union[str, NoneType]
            HTML template for the print footer. Should use the same format as the `headerTemplate`.
        print_background : Union[bool, NoneType]
            Print background graphics. Defaults to `false`.
        landscape : Union[bool, NoneType]
            Paper orientation. Defaults to `false`.
        page_ranges : Union[str, NoneType]
            Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.
        format : Union[str, NoneType]
            Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'.
        width : Union[float, str, NoneType]
            Paper width, accepts values labeled with units.
        height : Union[float, str, NoneType]
            Paper height, accepts values labeled with units.
        prefer_css_page_size : Union[bool, NoneType]
            Give any CSS `@page` size declared in the page priority over what is declared in `width` and `height` or `format`
            options. Defaults to `false`, which will scale the content to fit the paper size.
        margin : Union[{top: Union[float, str, NoneType], right: Union[float, str, NoneType], bottom: Union[float, str, NoneType], left: Union[float, str, NoneType]}, NoneType]
            Paper margins, defaults to none.
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the PDF to. If `path` is a relative path, then it is resolved relative to the current working
            directory. If no path is provided, the PDF won't be saved to the disk.

        Returns
        -------
        bytes
        """

        return mapping.from_maybe_impl(
            await self._async(
                "page.pdf",
                self._impl_obj.pdf(
                    scale=scale,
                    displayHeaderFooter=display_header_footer,
                    headerTemplate=header_template,
                    footerTemplate=footer_template,
                    printBackground=print_background,
                    landscape=landscape,
                    pageRanges=page_ranges,
                    format=format,
                    width=width,
                    height=height,
                    preferCSSPageSize=prefer_css_page_size,
                    margin=margin,
                    path=path,
                ),
            )
        )

    def expect_event(
        self, event: str, predicate: typing.Callable = None, *, timeout: float = None
    ) -> AsyncEventContextManager:
        """Page.expect_event

        Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
        value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

        ```py
        async with page.expect_event(\"framenavigated\") as event_info:
            await page.click(\"button\")
        frame = await event_info.value
        ```

        Parameters
        ----------
        event : str
            Event name, same one typically passed into `*.on(event)`.
        predicate : Union[Callable, NoneType]
            Receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_event(
                event=event, predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    def expect_console_message(
        self,
        predicate: typing.Optional[typing.Callable[["ConsoleMessage"], bool]] = None,
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["ConsoleMessage"]:
        """Page.expect_console_message

        Performs action and waits for a [ConoleMessage] to be logged by in the page. If predicate is provided, it passes
        `ConsoleMessage` value into the `predicate` function and waits for `predicate(message)` to return a truthy value. Will
        throw an error if the page is closed before the console event is fired.

        Parameters
        ----------
        predicate : Union[Callable[[ConsoleMessage], bool], NoneType]
            Receives the `ConsoleMessage` object and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager[ConsoleMessage]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_console_message(
                predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    def expect_download(
        self,
        predicate: typing.Optional[typing.Callable[["Download"], bool]] = None,
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["Download"]:
        """Page.expect_download

        Performs action and waits for a new `Download`. If predicate is provided, it passes `Download` value into the
        `predicate` function and waits for `predicate(download)` to return a truthy value. Will throw an error if the page is
        closed before the download event is fired.

        Parameters
        ----------
        predicate : Union[Callable[[Download], bool], NoneType]
            Receives the `Download` object and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager[Download]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_download(
                predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    def expect_file_chooser(
        self,
        predicate: typing.Optional[typing.Callable[["FileChooser"], bool]] = None,
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["FileChooser"]:
        """Page.expect_file_chooser

        Performs action and waits for a new `FileChooser` to be created. If predicate is provided, it passes `FileChooser` value
        into the `predicate` function and waits for `predicate(fileChooser)` to return a truthy value. Will throw an error if
        the page is closed before the file chooser is opened.

        Parameters
        ----------
        predicate : Union[Callable[[FileChooser], bool], NoneType]
            Receives the `FileChooser` object and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager[FileChooser]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_file_chooser(
                predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    def expect_navigation(
        self,
        *,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None
    ) -> AsyncEventContextManager["Response"]:
        """Page.expect_navigation

        Waits for the main frame navigation and returns the main resource response. In case of multiple redirects, the
        navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or
        navigation due to History API usage, the navigation will resolve with `null`.

        This resolves when the page navigates to a new URL or reloads. It is useful for when you run code which will indirectly
        cause the page to navigate. e.g. The click target has an `onclick` handler that triggers navigation from a `setTimeout`.
        Consider this example:

        ```py
        async with page.expect_navigation():
            await page.click(\"a.delayed-navigation\") # clicking the link will indirectly cause a navigation
        # Resolves after navigation has finished
        ```

        > NOTE: Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is
        considered a navigation.

        Shortcut for main frame's `frame.expect_navigation()`.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str, NoneType]
            A glob pattern, regex pattern or predicate receiving [URL] to match while waiting for the navigation.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.

        Returns
        -------
        EventContextManager[Response]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_navigation(
                url=self._wrap_handler(url), wait_until=wait_until, timeout=timeout
            ).future
        )

    def expect_popup(
        self,
        predicate: typing.Optional[typing.Callable[["Page"], bool]] = None,
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["Page"]:
        """Page.expect_popup

        Performs action and waits for a popup `Page`. If predicate is provided, it passes [Popup] value into the `predicate`
        function and waits for `predicate(page)` to return a truthy value. Will throw an error if the page is closed before the
        popup event is fired.

        Parameters
        ----------
        predicate : Union[Callable[[Page], bool], NoneType]
            Receives the `Page` object and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager[Page]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_popup(
                predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    def expect_request(
        self,
        url_or_predicate: typing.Union[
            str, typing.Pattern, typing.Callable[["Request"], bool]
        ],
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["Request"]:
        """Page.expect_request

        Waits for the matching request and returns it.

        ```py
        async with page.expect_request(\"http://example.com/resource\") as first:
            await page.click('button')
        first_request = await first.value

        async with page.expect_request(lambda request: request.url == \"http://example.com\" and request.method == \"get\") as second:
            await page.click('img')
        second_request = await second.value
        ```

        Parameters
        ----------
        url_or_predicate : Union[Callable[[Request], bool], Pattern, str]
            Request URL string, regex or predicate receiving `Request` object.
        timeout : Union[float, NoneType]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be
            changed by using the `page.set_default_timeout()` method.

        Returns
        -------
        EventContextManager[Request]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_request(
                url_or_predicate=self._wrap_handler(url_or_predicate), timeout=timeout
            ).future
        )

    def expect_response(
        self,
        url_or_predicate: typing.Union[
            str, typing.Pattern, typing.Callable[["Response"], bool]
        ],
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["Response"]:
        """Page.expect_response

        Returns the matched response.

        ```py
        async with page.expect_response(\"https://example.com/resource\") as response_info:
            await page.click(\"input\")
        response = response_info.value
        return response.ok

        # or with a lambda
        async with page.expect_response(lambda response: response.url == \"https://example.com\" and response.status === 200) as response_info:
            await page.click(\"input\")
        response = response_info.value
        return response.ok
        ```

        Parameters
        ----------
        url_or_predicate : Union[Callable[[Response], bool], Pattern, str]
            Request URL string, regex or predicate receiving `Response` object.
        timeout : Union[float, NoneType]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be
            changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        EventContextManager[Response]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_response(
                url_or_predicate=self._wrap_handler(url_or_predicate), timeout=timeout
            ).future
        )

    def expect_worker(
        self,
        predicate: typing.Optional[typing.Callable[["Worker"], bool]] = None,
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["Worker"]:
        """Page.expect_worker

        Performs action and waits for a new `Worker`. If predicate is provided, it passes `Worker` value into the `predicate`
        function and waits for `predicate(worker)` to return a truthy value. Will throw an error if the page is closed before
        the worker event is fired.

        Parameters
        ----------
        predicate : Union[Callable[[Worker], bool], NoneType]
            Receives the `Worker` object and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager[Worker]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_worker(
                predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )


mapping.register(PageImpl, Page)


class BrowserContext(AsyncBase):
    def __init__(self, obj: BrowserContextImpl):
        super().__init__(obj)

    @property
    def pages(self) -> typing.List["Page"]:
        """BrowserContext.pages

        Returns all open pages in the context.

        Returns
        -------
        List[Page]
        """
        return mapping.from_impl_list(self._impl_obj.pages)

    @property
    def browser(self) -> typing.Optional["Browser"]:
        """BrowserContext.browser

        Returns the browser instance of the context. If it was launched as a persistent context null gets returned.

        Returns
        -------
        Union[Browser, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.browser)

    def set_default_navigation_timeout(self, timeout: float) -> NoneType:
        """BrowserContext.set_default_navigation_timeout

        This setting will change the default maximum navigation time for the following methods and related shortcuts:
        - `page.go_back()`
        - `page.go_forward()`
        - `page.goto()`
        - `page.reload()`
        - `page.set_content()`
        - `page.expect_navigation()`

        > NOTE: `page.set_default_navigation_timeout()` and `page.set_default_timeout()` take priority over
        `browser_context.set_default_navigation_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum navigation time in milliseconds
        """

        return mapping.from_maybe_impl(
            self._impl_obj.set_default_navigation_timeout(timeout=timeout)
        )

    def set_default_timeout(self, timeout: float) -> NoneType:
        """BrowserContext.set_default_timeout

        This setting will change the default maximum time for all the methods accepting `timeout` option.

        > NOTE: `page.set_default_navigation_timeout()`, `page.set_default_timeout()` and
        `browser_context.set_default_navigation_timeout()` take priority over `browser_context.set_default_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum time in milliseconds
        """

        return mapping.from_maybe_impl(
            self._impl_obj.set_default_timeout(timeout=timeout)
        )

    async def new_page(self) -> "Page":
        """BrowserContext.new_page

        Creates a new page in the browser context.

        Returns
        -------
        Page
        """

        return mapping.from_impl(
            await self._async("browser_context.new_page", self._impl_obj.new_page())
        )

    async def cookies(
        self, urls: typing.Union[str, typing.List[str]] = None
    ) -> typing.List[Cookie]:
        """BrowserContext.cookies

        If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those URLs
        are returned.

        Parameters
        ----------
        urls : Union[List[str], str, NoneType]
            Optional list of URLs.

        Returns
        -------
        List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Lax", "None", "Strict", NoneType]}]
        """

        return mapping.from_impl_list(
            await self._async(
                "browser_context.cookies", self._impl_obj.cookies(urls=urls)
            )
        )

    async def add_cookies(self, cookies: typing.List[Cookie]) -> NoneType:
        """BrowserContext.add_cookies

        Adds cookies into this browser context. All pages within this context will have these cookies installed. Cookies can be
        obtained via `browser_context.cookies()`.

        ```py
        await browser_context.add_cookies([cookie_object1, cookie_object2])
        ```

        Parameters
        ----------
        cookies : List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Lax", "None", "Strict", NoneType]}]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.add_cookies",
                self._impl_obj.add_cookies(cookies=cookies),
            )
        )

    async def clear_cookies(self) -> NoneType:
        """BrowserContext.clear_cookies

        Clears context cookies.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.clear_cookies", self._impl_obj.clear_cookies()
            )
        )

    async def grant_permissions(
        self, permissions: typing.List[str], *, origin: str = None
    ) -> NoneType:
        """BrowserContext.grant_permissions

        Grants specified permissions to the browser context. Only grants corresponding permissions to the given origin if
        specified.

        Parameters
        ----------
        permissions : List[str]
            A permission or an array of permissions to grant. Permissions can be one of the following values:
            - `'geolocation'`
            - `'midi'`
            - `'midi-sysex'` (system-exclusive midi)
            - `'notifications'`
            - `'push'`
            - `'camera'`
            - `'microphone'`
            - `'background-sync'`
            - `'ambient-light-sensor'`
            - `'accelerometer'`
            - `'gyroscope'`
            - `'magnetometer'`
            - `'accessibility-events'`
            - `'clipboard-read'`
            - `'clipboard-write'`
            - `'payment-handler'`
        origin : Union[str, NoneType]
            The [origin] to grant permissions to, e.g. "https://example.com".
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.grant_permissions",
                self._impl_obj.grant_permissions(
                    permissions=permissions, origin=origin
                ),
            )
        )

    async def clear_permissions(self) -> NoneType:
        """BrowserContext.clear_permissions

        Clears all permission overrides for the browser context.

        ```py
        context = await browser.new_context()
        await context.grant_permissions([\"clipboard-read\"])
        # do stuff ..
        context.clear_permissions()
        ```
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.clear_permissions", self._impl_obj.clear_permissions()
            )
        )

    async def set_geolocation(self, geolocation: Geolocation = None) -> NoneType:
        """BrowserContext.set_geolocation

        Sets the context's geolocation. Passing `null` or `undefined` emulates position unavailable.

        ```py
        await browser_context.set_geolocation({\"latitude\": 59.95, \"longitude\": 30.31667})
        ```

        > NOTE: Consider using `browser_context.grant_permissions()` to grant permissions for the browser context pages to
        read its geolocation.

        Parameters
        ----------
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.set_geolocation",
                self._impl_obj.set_geolocation(geolocation=geolocation),
            )
        )

    async def set_extra_http_headers(self, headers: typing.Dict[str, str]) -> NoneType:
        """BrowserContext.set_extra_http_headers

        The extra HTTP headers will be sent with every request initiated by any page in the context. These headers are merged
        with page-specific extra HTTP headers set with `page.set_extra_http_headers()`. If page overrides a particular
        header, page-specific header value will be used instead of the browser context header value.

        > NOTE: `browser_context.set_extra_http_headers()` does not guarantee the order of headers in the outgoing requests.

        Parameters
        ----------
        headers : Dict[str, str]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.set_extra_http_headers",
                self._impl_obj.set_extra_http_headers(headers=mapping.to_impl(headers)),
            )
        )

    async def set_offline(self, offline: bool) -> NoneType:
        """BrowserContext.set_offline

        Parameters
        ----------
        offline : bool
            Whether to emulate network being offline for the browser context.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.set_offline",
                self._impl_obj.set_offline(offline=offline),
            )
        )

    async def add_init_script(
        self, script: str = None, *, path: typing.Union[str, pathlib.Path] = None
    ) -> NoneType:
        """BrowserContext.add_init_script

        Adds a script which would be evaluated in one of the following scenarios:
        - Whenever a page is created in the browser context or is navigated.
        - Whenever a child frame is attached or navigated in any page in the browser context. In this case, the script is
          evaluated in the context of the newly attached frame.

        The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend
        the JavaScript environment, e.g. to seed `Math.random`.

        An example of overriding `Math.random` before the page loads:

        ```py
        # in your playwright script, assuming the preload.js file is in same directory.
        await browser_context.add_init_script(path=\"preload.js\")
        ```

        > NOTE: The order of evaluation of multiple scripts installed via `browser_context.add_init_script()` and
        `page.add_init_script()` is not defined.

        Parameters
        ----------
        script : Union[str, NoneType]
            Script to be evaluated in all pages in the browser context. Optional.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working
            directory. Optional.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.add_init_script",
                self._impl_obj.add_init_script(script=script, path=path),
            )
        )

    async def expose_binding(
        self, name: str, callback: typing.Callable, *, handle: bool = None
    ) -> NoneType:
        """BrowserContext.expose_binding

        The method adds a function called `name` on the `window` object of every frame in every page in the context. When
        called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`. If
        the `callback` returns a [Promise], it will be awaited.

        The first argument of the `callback` function contains information about the caller: `{ browserContext: BrowserContext,
        page: Page, frame: Frame }`.

        See `page.expose_binding()` for page-only version.

        An example of exposing page URL to all frames in all pages in the context:

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            webkit = playwright.webkit
            browser = await webkit.launch(headless=false)
            context = await browser.new_context()
            await context.expose_binding(\"pageURL\", lambda source: source[\"page\"].url)
            page = await context.new_page()
            await page.set_content(\"\"\"
            <script>
              async function onClick() {
                document.querySelector('div').textContent = await window.pageURL();
              }
            </script>
            <button onclick=\"onClick()\">Click me</button>
            <div></div>
            \"\"\")
            await page.click(\"button\")

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        An example of passing an element handle:

        ```py
        async def print(source, element):
            print(await element.text_content())

        await context.expose_binding(\"clicked\", print, handle=true)
        await page.set_content(\"\"\"
          <script>
            document.addEventListener('click', event => window.clicked(event.target));
          </script>
          <div>Click me</div>
          <div>Or click me</div>
        \"\"\")
        ```

        Parameters
        ----------
        name : str
            Name of the function on the window object.
        callback : Callable
            Callback function that will be called in the Playwright's context.
        handle : Union[bool, NoneType]
            Whether to pass the argument as a handle, instead of passing by value. When passing a handle, only one argument is
            supported. When passing by value, multiple arguments are supported.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.expose_binding",
                self._impl_obj.expose_binding(
                    name=name, callback=self._wrap_handler(callback), handle=handle
                ),
            )
        )

    async def expose_function(self, name: str, callback: typing.Callable) -> NoneType:
        """BrowserContext.expose_function

        The method adds a function called `name` on the `window` object of every frame in every page in the context. When
        called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

        If the `callback` returns a [Promise], it will be awaited.

        See `page.expose_function()` for page-only version.

        An example of adding an `md5` function to all pages in the context:

        ```py
        import asyncio
        import hashlib
        from playwright.async_api import async_playwright

        async def sha1(text):
            m = hashlib.sha1()
            m.update(bytes(text, \"utf8\"))
            return m.hexdigest()

        async def run(playwright):
            webkit = playwright.webkit
            browser = await webkit.launch(headless=False)
            context = await browser.new_context()
            await context.expose_function(\"sha1\", sha1)
            page = await context.new_page()
            await page.set_content(\"\"\"
                <script>
                  async function onClick() {
                    document.querySelector('div').textContent = await window.sha1('PLAYWRIGHT');
                  }
                </script>
                <button onclick=\"onClick()\">Click me</button>
                <div></div>
            \"\"\")
            await page.click(\"button\")

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        Parameters
        ----------
        name : str
            Name of the function on the window object.
        callback : Callable
            Callback function that will be called in the Playwright's context.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.expose_function",
                self._impl_obj.expose_function(
                    name=name, callback=self._wrap_handler(callback)
                ),
            )
        )

    async def route(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ],
    ) -> NoneType:
        """BrowserContext.route

        Routing provides the capability to modify network requests that are made by any page in the browser context. Once route
        is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

        An example of a naïve handler that aborts all image requests:

        ```py
        context = await browser.new_context()
        page = await context.new_page()
        await context.route(\"**/*.{png,jpg,jpeg}\", lambda route: route.abort())
        await page.goto(\"https://example.com\")
        await browser.close()
        ```

        or the same snippet using a regex pattern instead:

        ```py
        context = await browser.new_context()
        page = await context.new_page()
        await context.route(re.compile(r\"(\\.png$)|(\\.jpg$)\"), lambda route: route.abort())
        page = await context.new_page()
        await page.goto(\"https://example.com\")
        await browser.close()
        ```

        Page routes (set up with `page.route()`) take precedence over browser context routes when request matches both
        handlers.

        > NOTE: Enabling routing disables http cache.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] to match while routing.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any]]
            handler function to route the request.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.route",
                self._impl_obj.route(
                    url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                ),
            )
        )

    async def unroute(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ] = None,
    ) -> NoneType:
        """BrowserContext.unroute

        Removes a route created with `browser_context.route()`. When `handler` is not specified, removes all routes for
        the `url`.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] used to register a routing with
            `browser_context.route()`.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any], NoneType]
            Optional handler function used to register a routing with `browser_context.route()`.
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.unroute",
                self._impl_obj.unroute(
                    url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                ),
            )
        )

    def expect_event(
        self, event: str, predicate: typing.Callable = None, *, timeout: float = None
    ) -> AsyncEventContextManager:
        """BrowserContext.expect_event

        Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
        value. Will throw an error if the context closes before the event is fired. Returns the event data value.

        ```py
        async with context.expect_event(\"page\") as event_info:
            await page.click(\"button\")
        page = await event_info.value
        ```

        Parameters
        ----------
        event : str
            Event name, same one would pass into `browserContext.on(event)`.
        predicate : Union[Callable, NoneType]
            Receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_event(
                event=event, predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )

    async def close(self) -> NoneType:
        """BrowserContext.close

        Closes the browser context. All the pages that belong to the browser context will be closed.

        > NOTE: The default browser context cannot be closed.
        """

        return mapping.from_maybe_impl(
            await self._async("browser_context.close", self._impl_obj.close())
        )

    async def storage_state(
        self, *, path: typing.Union[str, pathlib.Path] = None
    ) -> StorageState:
        """BrowserContext.storage_state

        Returns storage state for this browser context, contains current cookies and local storage snapshot.

        Parameters
        ----------
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the storage state to. If `path` is a relative path, then it is resolved relative to current
            working directory. If no path is provided, storage state is still returned, but won't be saved to the disk.

        Returns
        -------
        {cookies: Union[List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Lax", "None", "Strict", NoneType]}], NoneType], origins: Union[List[{origin: str, localStorage: List[{name: str, value: str}]}], NoneType]}
        """

        return mapping.from_impl(
            await self._async(
                "browser_context.storage_state", self._impl_obj.storage_state(path=path)
            )
        )

    async def wait_for_event(
        self, event: str, predicate: typing.Callable = None, *, timeout: float = None
    ) -> typing.Any:
        """BrowserContext.wait_for_event

        > NOTE: In most cases, you should use `browser_context.expect_event()`.

        Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function and
        waits for `predicate(event)` to return a truthy value. Will throw an error if the socket is closed before the `event` is
        fired.

        Parameters
        ----------
        event : str
            Event name, same one typically passed into `*.on(event)`.
        predicate : Union[Callable, NoneType]
            Receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        Any
        """

        return mapping.from_maybe_impl(
            await self._async(
                "browser_context.wait_for_event",
                self._impl_obj.wait_for_event(
                    event=event,
                    predicate=self._wrap_handler(predicate),
                    timeout=timeout,
                ),
            )
        )

    def expect_page(
        self,
        predicate: typing.Optional[typing.Callable[["Page"], bool]] = None,
        *,
        timeout: float = None
    ) -> AsyncEventContextManager["Page"]:
        """BrowserContext.expect_page

        Performs action and waits for a new `Page` to be created in the context. If predicate is provided, it passes `Page`
        value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error if
        the context closes before new `Page` is created.

        Parameters
        ----------
        predicate : Union[Callable[[Page], bool], NoneType]
            Receives the `Page` object and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        EventContextManager[Page]
        """

        return AsyncEventContextManager(
            self._impl_obj.expect_page(
                predicate=self._wrap_handler(predicate), timeout=timeout
            ).future
        )


mapping.register(BrowserContextImpl, BrowserContext)


class CDPSession(AsyncBase):
    def __init__(self, obj: CDPSessionImpl):
        super().__init__(obj)

    async def send(self, method: str, params: typing.Dict = None) -> typing.Dict:
        """CDPSession.send

        Parameters
        ----------
        method : str
            protocol method name
        params : Union[Dict, NoneType]
            Optional method parameters

        Returns
        -------
        Dict
        """

        return mapping.from_maybe_impl(
            await self._async(
                "cdp_session.send",
                self._impl_obj.send(method=method, params=mapping.to_impl(params)),
            )
        )

    async def detach(self) -> NoneType:
        """CDPSession.detach

        Detaches the CDPSession from the target. Once detached, the CDPSession object won't emit any events and can't be used to
        send messages.
        """

        return mapping.from_maybe_impl(
            await self._async("cdp_session.detach", self._impl_obj.detach())
        )


mapping.register(CDPSessionImpl, CDPSession)


class ChromiumBrowserContext(BrowserContext):
    def __init__(self, obj: ChromiumBrowserContextImpl):
        super().__init__(obj)

    @property
    def background_pages(self) -> typing.List["Page"]:
        """ChromiumBrowserContext.background_pages

        All existing background pages in the context.

        Returns
        -------
        List[Page]
        """
        return mapping.from_impl_list(self._impl_obj.background_pages)

    @property
    def service_workers(self) -> typing.List["Worker"]:
        """ChromiumBrowserContext.service_workers

        All existing service workers in the context.

        Returns
        -------
        List[Worker]
        """
        return mapping.from_impl_list(self._impl_obj.service_workers)

    async def new_cdp_session(self, page: "Page") -> "CDPSession":
        """ChromiumBrowserContext.new_cdp_session

        Returns the newly created session.

        Parameters
        ----------
        page : Page
            Page to create new session for.

        Returns
        -------
        CDPSession
        """

        return mapping.from_impl(
            await self._async(
                "chromium_browser_context.new_cdp_session",
                self._impl_obj.new_cdp_session(page=page._impl_obj),
            )
        )


mapping.register(ChromiumBrowserContextImpl, ChromiumBrowserContext)


class Browser(AsyncBase):
    def __init__(self, obj: BrowserImpl):
        super().__init__(obj)

    @property
    def contexts(self) -> typing.List["BrowserContext"]:
        """Browser.contexts

        Returns an array of all open browser contexts. In a newly created browser, this will return zero browser contexts.

        ```py
        browser = await pw.webkit.launch()
        print(len(browser.contexts())) # prints `0`
        context = await browser.new_context()
        print(len(browser.contexts())) # prints `1`
        ```

        Returns
        -------
        List[BrowserContext]
        """
        return mapping.from_impl_list(self._impl_obj.contexts)

    @property
    def version(self) -> str:
        """Browser.version

        Returns the browser version.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.version)

    def is_connected(self) -> bool:
        """Browser.is_connected

        Indicates that the browser is connected.

        Returns
        -------
        bool
        """

        return mapping.from_maybe_impl(self._impl_obj.is_connected())

    async def new_context(
        self,
        *,
        viewport: ViewportSize = None,
        no_viewport: bool = None,
        ignore_https_errors: bool = None,
        java_script_enabled: bool = None,
        bypass_csp: bool = None,
        user_agent: str = None,
        locale: str = None,
        timezone_id: str = None,
        geolocation: Geolocation = None,
        permissions: typing.List[str] = None,
        extra_http_headers: typing.Optional[typing.Dict[str, str]] = None,
        offline: bool = None,
        http_credentials: HttpCredentials = None,
        device_scale_factor: float = None,
        is_mobile: bool = None,
        has_touch: bool = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
        accept_downloads: bool = None,
        default_browser_type: str = None,
        proxy: ProxySettings = None,
        record_har_path: typing.Union[str, pathlib.Path] = None,
        record_har_omit_content: bool = None,
        record_video_dir: typing.Union[str, pathlib.Path] = None,
        record_video_size: ViewportSize = None,
        storage_state: typing.Union[StorageState, str, pathlib.Path] = None
    ) -> "BrowserContext":
        """Browser.new_context

        Creates a new browser context. It won't share cookies/cache with other browser contexts.

        ```py
        browser = await playwright.firefox.launch() # or \"chromium\" or \"webkit\".
        # create a new incognito browser context.
        context = await browser.new_context()
        # create a new page in a pristine context.
        page = await context.new_page()
        await page.goto(\"https://example.com\")
        ```

        Parameters
        ----------
        viewport : Union[{width: int, height: int}, NoneType]
            Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport.
        no_viewport : Union[bool, NoneType]
            Does not enforce fixed viewport, allows resizing window in the headed mode.
        ignore_https_errors : Union[bool, NoneType]
            Whether to ignore HTTPS errors during navigation. Defaults to `false`.
        java_script_enabled : Union[bool, NoneType]
            Whether or not to enable JavaScript in the context. Defaults to `true`.
        bypass_csp : Union[bool, NoneType]
            Toggles bypassing page's Content-Security-Policy.
        user_agent : Union[str, NoneType]
            Specific user agent to use in this context.
        locale : Union[str, NoneType]
            Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language`
            request header value as well as number and date formatting rules.
        timezone_id : Union[str, NoneType]
            Changes the timezone of the context. See
            [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)
            for a list of supported timezone IDs.
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        permissions : Union[List[str], NoneType]
            A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more
            details.
        extra_http_headers : Union[Dict[str, str], NoneType]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        offline : Union[bool, NoneType]
            Whether to emulate network being offline. Defaults to `false`.
        http_credentials : Union[{username: str, password: str}, NoneType]
            Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).
        device_scale_factor : Union[float, NoneType]
            Specify device scale factor (can be thought of as dpr). Defaults to `1`.
        is_mobile : Union[bool, NoneType]
            Whether the `meta viewport` tag is taken into account and touch events are enabled. Defaults to `false`. Not supported
            in Firefox.
        has_touch : Union[bool, NoneType]
            Specifies if viewport supports touch events. Defaults to false.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. See
            `page.emulate_media()` for more details. Defaults to `'light'`.
        accept_downloads : Union[bool, NoneType]
            Whether to automatically download all the attachments. Defaults to `false` where all the downloads are canceled.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings to use with this context. Note that browser needs to be launched with the global proxy for this
            option to work. If all contexts override the proxy, global proxy will be never used and can be any string, for example
            `launch({ proxy: { server: 'per-context' } })`.
        record_har_path : Union[pathlib.Path, str, NoneType]
            Path on the filesystem to write the HAR file to.
        record_har_omit_content : Union[bool, NoneType]
            Optional setting to control whether to omit request content from the HAR. Defaults to `false`.
        record_video_dir : Union[pathlib.Path, str, NoneType]
            Path to the directory to put videos into.
        record_video_size : Union[{width: int, height: int}, NoneType]
            Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into
            800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will
            be scaled down if necessary to fit the specified size.
        storage_state : Union[pathlib.Path, str, {cookies: Union[List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Lax", "None", "Strict", NoneType]}], NoneType], origins: Union[List[{origin: str, localStorage: List[{name: str, value: str}]}], NoneType]}, NoneType]
            Populates context with given storage state. This option can be used to initialize context with logged-in information
            obtained via `browser_context.storage_state()`. Either a path to the file with saved storage, or an object with
            the following fields:

        Returns
        -------
        BrowserContext
        """

        return mapping.from_impl(
            await self._async(
                "browser.new_context",
                self._impl_obj.new_context(
                    viewport=viewport,
                    noViewport=no_viewport,
                    ignoreHTTPSErrors=ignore_https_errors,
                    javaScriptEnabled=java_script_enabled,
                    bypassCSP=bypass_csp,
                    userAgent=user_agent,
                    locale=locale,
                    timezoneId=timezone_id,
                    geolocation=geolocation,
                    permissions=permissions,
                    extraHTTPHeaders=mapping.to_impl(extra_http_headers),
                    offline=offline,
                    httpCredentials=http_credentials,
                    deviceScaleFactor=device_scale_factor,
                    isMobile=is_mobile,
                    hasTouch=has_touch,
                    colorScheme=color_scheme,
                    acceptDownloads=accept_downloads,
                    defaultBrowserType=default_browser_type,
                    proxy=proxy,
                    recordHarPath=record_har_path,
                    recordHarOmitContent=record_har_omit_content,
                    recordVideoDir=record_video_dir,
                    recordVideoSize=record_video_size,
                    storageState=storage_state,
                ),
            )
        )

    async def new_page(
        self,
        *,
        viewport: ViewportSize = None,
        no_viewport: bool = None,
        ignore_https_errors: bool = None,
        java_script_enabled: bool = None,
        bypass_csp: bool = None,
        user_agent: str = None,
        locale: str = None,
        timezone_id: str = None,
        geolocation: Geolocation = None,
        permissions: typing.List[str] = None,
        extra_http_headers: typing.Optional[typing.Dict[str, str]] = None,
        offline: bool = None,
        http_credentials: HttpCredentials = None,
        device_scale_factor: float = None,
        is_mobile: bool = None,
        has_touch: bool = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
        accept_downloads: bool = None,
        default_browser_type: str = None,
        proxy: ProxySettings = None,
        record_har_path: typing.Union[str, pathlib.Path] = None,
        record_har_omit_content: bool = None,
        record_video_dir: typing.Union[str, pathlib.Path] = None,
        record_video_size: ViewportSize = None,
        storage_state: typing.Union[StorageState, str, pathlib.Path] = None
    ) -> "Page":
        """Browser.new_page

        Creates a new page in a new browser context. Closing this page will close the context as well.

        This is a convenience API that should only be used for the single-page scenarios and short snippets. Production code and
        testing frameworks should explicitly create `browser.new_context()` followed by the
        `browser_context.new_page()` to control their exact life times.

        Parameters
        ----------
        viewport : Union[{width: int, height: int}, NoneType]
            Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport.
        no_viewport : Union[bool, NoneType]
            Does not enforce fixed viewport, allows resizing window in the headed mode.
        ignore_https_errors : Union[bool, NoneType]
            Whether to ignore HTTPS errors during navigation. Defaults to `false`.
        java_script_enabled : Union[bool, NoneType]
            Whether or not to enable JavaScript in the context. Defaults to `true`.
        bypass_csp : Union[bool, NoneType]
            Toggles bypassing page's Content-Security-Policy.
        user_agent : Union[str, NoneType]
            Specific user agent to use in this context.
        locale : Union[str, NoneType]
            Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language`
            request header value as well as number and date formatting rules.
        timezone_id : Union[str, NoneType]
            Changes the timezone of the context. See
            [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)
            for a list of supported timezone IDs.
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        permissions : Union[List[str], NoneType]
            A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more
            details.
        extra_http_headers : Union[Dict[str, str], NoneType]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        offline : Union[bool, NoneType]
            Whether to emulate network being offline. Defaults to `false`.
        http_credentials : Union[{username: str, password: str}, NoneType]
            Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).
        device_scale_factor : Union[float, NoneType]
            Specify device scale factor (can be thought of as dpr). Defaults to `1`.
        is_mobile : Union[bool, NoneType]
            Whether the `meta viewport` tag is taken into account and touch events are enabled. Defaults to `false`. Not supported
            in Firefox.
        has_touch : Union[bool, NoneType]
            Specifies if viewport supports touch events. Defaults to false.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. See
            `page.emulate_media()` for more details. Defaults to `'light'`.
        accept_downloads : Union[bool, NoneType]
            Whether to automatically download all the attachments. Defaults to `false` where all the downloads are canceled.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings to use with this context. Note that browser needs to be launched with the global proxy for this
            option to work. If all contexts override the proxy, global proxy will be never used and can be any string, for example
            `launch({ proxy: { server: 'per-context' } })`.
        record_har_path : Union[pathlib.Path, str, NoneType]
            Path on the filesystem to write the HAR file to.
        record_har_omit_content : Union[bool, NoneType]
            Optional setting to control whether to omit request content from the HAR. Defaults to `false`.
        record_video_dir : Union[pathlib.Path, str, NoneType]
            Path to the directory to put videos into.
        record_video_size : Union[{width: int, height: int}, NoneType]
            Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into
            800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will
            be scaled down if necessary to fit the specified size.
        storage_state : Union[pathlib.Path, str, {cookies: Union[List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Lax", "None", "Strict", NoneType]}], NoneType], origins: Union[List[{origin: str, localStorage: List[{name: str, value: str}]}], NoneType]}, NoneType]
            Populates context with given storage state. This option can be used to initialize context with logged-in information
            obtained via `browser_context.storage_state()`. Either a path to the file with saved storage, or an object with
            the following fields:

        Returns
        -------
        Page
        """

        return mapping.from_impl(
            await self._async(
                "browser.new_page",
                self._impl_obj.new_page(
                    viewport=viewport,
                    noViewport=no_viewport,
                    ignoreHTTPSErrors=ignore_https_errors,
                    javaScriptEnabled=java_script_enabled,
                    bypassCSP=bypass_csp,
                    userAgent=user_agent,
                    locale=locale,
                    timezoneId=timezone_id,
                    geolocation=geolocation,
                    permissions=permissions,
                    extraHTTPHeaders=mapping.to_impl(extra_http_headers),
                    offline=offline,
                    httpCredentials=http_credentials,
                    deviceScaleFactor=device_scale_factor,
                    isMobile=is_mobile,
                    hasTouch=has_touch,
                    colorScheme=color_scheme,
                    acceptDownloads=accept_downloads,
                    defaultBrowserType=default_browser_type,
                    proxy=proxy,
                    recordHarPath=record_har_path,
                    recordHarOmitContent=record_har_omit_content,
                    recordVideoDir=record_video_dir,
                    recordVideoSize=record_video_size,
                    storageState=storage_state,
                ),
            )
        )

    async def close(self) -> NoneType:
        """Browser.close

        In case this browser is obtained using `browser_type.launch()`, closes the browser and all of its pages (if any
        were opened).

        In case this browser is connected to, clears all created contexts belonging to this browser and disconnects from the
        browser server.

        The `Browser` object itself is considered to be disposed and cannot be used anymore.
        """

        return mapping.from_maybe_impl(
            await self._async("browser.close", self._impl_obj.close())
        )


mapping.register(BrowserImpl, Browser)


class BrowserType(AsyncBase):
    def __init__(self, obj: BrowserTypeImpl):
        super().__init__(obj)

    @property
    def name(self) -> str:
        """BrowserType.name

        Returns browser name. For example: `'chromium'`, `'webkit'` or `'firefox'`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.name)

    @property
    def executable_path(self) -> str:
        """BrowserType.executable_path

        A path where Playwright expects to find a bundled browser executable.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.executable_path)

    async def launch(
        self,
        *,
        executable_path: typing.Union[str, pathlib.Path] = None,
        channel: str = None,
        args: typing.List[str] = None,
        ignore_default_args: typing.Union[bool, typing.List[str]] = None,
        handle_sigint: bool = None,
        handle_sigterm: bool = None,
        handle_sighup: bool = None,
        timeout: float = None,
        env: typing.Optional[typing.Dict[str, typing.Union[str, float, bool]]] = None,
        headless: bool = None,
        devtools: bool = None,
        proxy: ProxySettings = None,
        downloads_path: typing.Union[str, pathlib.Path] = None,
        slow_mo: float = None,
        chromium_sandbox: bool = None,
        firefox_user_prefs: typing.Optional[
            typing.Dict[str, typing.Union[str, float, bool]]
        ] = None
    ) -> "Browser":
        """BrowserType.launch

        Returns the browser instance.

        You can use `ignoreDefaultArgs` to filter out `--mute-audio` from default arguments:

        ```py
        browser = await playwright.chromium.launch( # or \"firefox\" or \"webkit\".
            ignore_default_args=[\"--mute-audio\"]
        )
        ```

        > **Chromium-only** Playwright can also be used to control the Google Chrome or Microsoft Edge browsers, but it works
        best with the version of Chromium it is bundled with. There is no guarantee it will work with any other version. Use
        `executablePath` option with extreme caution.
        >
        > If Google Chrome (rather than Chromium) is preferred, a
        [Chrome Canary](https://www.google.com/chrome/browser/canary.html) or
        [Dev Channel](https://www.chromium.org/getting-involved/dev-channel) build is suggested.
        >
        > Stock browsers like Google Chrome and Microsoft Edge are suitable for tests that require proprietary media codecs for
        video playback. See
        [this article](https://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/) for other
        differences between Chromium and Chrome.
        [This article](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/chromium_browser_vs_google_chrome.md)
        describes some differences for Linux users.

        Parameters
        ----------
        executable_path : Union[pathlib.Path, str, NoneType]
            Path to a browser executable to run instead of the bundled one. If `executablePath` is a relative path, then it is
            resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox
            or WebKit, use at your own risk.
        channel : Union[str, NoneType]
            Chromium distribution channel, one of
            - chrome
            - chrome-beta
            - chrome-dev
            - chrome-canary
            - msedge
            - msedge-beta
            - msedge-dev
            - msedge-canary
        args : Union[List[str], NoneType]
            Additional arguments to pass to the browser instance. The list of Chromium flags can be found
            [here](http://peter.sh/experiments/chromium-command-line-switches/).
        ignore_default_args : Union[List[str], bool, NoneType]
            If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is
            given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`.
        handle_sigint : Union[bool, NoneType]
            Close the browser process on Ctrl-C. Defaults to `true`.
        handle_sigterm : Union[bool, NoneType]
            Close the browser process on SIGTERM. Defaults to `true`.
        handle_sighup : Union[bool, NoneType]
            Close the browser process on SIGHUP. Defaults to `true`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds to wait for the browser instance to start. Defaults to `30000` (30 seconds). Pass `0` to
            disable timeout.
        env : Union[Dict[str, Union[bool, float, str]], NoneType]
            Specify environment variables that will be visible to the browser. Defaults to `process.env`.
        headless : Union[bool, NoneType]
            Whether to run browser in headless mode. More details for
            [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode). Defaults to `true` unless the
            `devtools` option is `true`.
        devtools : Union[bool, NoneType]
            **Chromium-only** Whether to auto-open a Developer Tools panel for each tab. If this option is `true`, the `headless`
            option will be set `false`.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings.
        downloads_path : Union[pathlib.Path, str, NoneType]
            If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is
            deleted when browser is closed.
        slow_mo : Union[float, NoneType]
            Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on.
        chromium_sandbox : Union[bool, NoneType]
            Enable Chromium sandboxing. Defaults to `false`.
        firefox_user_prefs : Union[Dict[str, Union[bool, float, str]], NoneType]
            Firefox user preferences. Learn more about the Firefox user preferences at
            [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).

        Returns
        -------
        Browser
        """

        return mapping.from_impl(
            await self._async(
                "browser_type.launch",
                self._impl_obj.launch(
                    executablePath=executable_path,
                    channel=channel,
                    args=args,
                    ignoreDefaultArgs=ignore_default_args,
                    handleSIGINT=handle_sigint,
                    handleSIGTERM=handle_sigterm,
                    handleSIGHUP=handle_sighup,
                    timeout=timeout,
                    env=mapping.to_impl(env),
                    headless=headless,
                    devtools=devtools,
                    proxy=proxy,
                    downloadsPath=downloads_path,
                    slowMo=slow_mo,
                    chromiumSandbox=chromium_sandbox,
                    firefoxUserPrefs=mapping.to_impl(firefox_user_prefs),
                ),
            )
        )

    async def launch_persistent_context(
        self,
        user_data_dir: typing.Union[str, pathlib.Path],
        *,
        channel: str = None,
        executable_path: typing.Union[str, pathlib.Path] = None,
        args: typing.List[str] = None,
        ignore_default_args: typing.Union[bool, typing.List[str]] = None,
        handle_sigint: bool = None,
        handle_sigterm: bool = None,
        handle_sighup: bool = None,
        timeout: float = None,
        env: typing.Optional[typing.Dict[str, typing.Union[str, float, bool]]] = None,
        headless: bool = None,
        devtools: bool = None,
        proxy: ProxySettings = None,
        downloads_path: typing.Union[str, pathlib.Path] = None,
        slow_mo: float = None,
        viewport: ViewportSize = None,
        no_viewport: bool = None,
        ignore_https_errors: bool = None,
        java_script_enabled: bool = None,
        bypass_csp: bool = None,
        user_agent: str = None,
        locale: str = None,
        timezone_id: str = None,
        geolocation: Geolocation = None,
        permissions: typing.List[str] = None,
        extra_http_headers: typing.Optional[typing.Dict[str, str]] = None,
        offline: bool = None,
        http_credentials: HttpCredentials = None,
        device_scale_factor: float = None,
        is_mobile: bool = None,
        has_touch: bool = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
        accept_downloads: bool = None,
        chromium_sandbox: bool = None,
        record_har_path: typing.Union[str, pathlib.Path] = None,
        record_har_omit_content: bool = None,
        record_video_dir: typing.Union[str, pathlib.Path] = None,
        record_video_size: ViewportSize = None
    ) -> "BrowserContext":
        """BrowserType.launch_persistent_context

        Returns the persistent browser context instance.

        Launches browser that uses persistent storage located at `userDataDir` and returns the only context. Closing this
        context will automatically close the browser.

        Parameters
        ----------
        user_data_dir : Union[pathlib.Path, str]
            Path to a User Data Directory, which stores browser session data like cookies and local storage. More details for
            [Chromium](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#introduction) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options#User_Profile). Note that Chromium's user
            data directory is the **parent** directory of the "Profile Path" seen at `chrome://version`.
        channel : Union[str, NoneType]
            Chromium distribution channel, one of
            - chrome
            - chrome-beta
            - chrome-dev
            - chrome-canary
            - msedge
            - msedge-beta
            - msedge-dev
            - msedge-canary
        executable_path : Union[pathlib.Path, str, NoneType]
            Path to a browser executable to run instead of the bundled one. If `executablePath` is a relative path, then it is
            resolved relative to the current working directory. **BEWARE**: Playwright is only guaranteed to work with the bundled
            Chromium, Firefox or WebKit, use at your own risk.
        args : Union[List[str], NoneType]
            Additional arguments to pass to the browser instance. The list of Chromium flags can be found
            [here](http://peter.sh/experiments/chromium-command-line-switches/).
        ignore_default_args : Union[List[str], bool, NoneType]
            If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is
            given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`.
        handle_sigint : Union[bool, NoneType]
            Close the browser process on Ctrl-C. Defaults to `true`.
        handle_sigterm : Union[bool, NoneType]
            Close the browser process on SIGTERM. Defaults to `true`.
        handle_sighup : Union[bool, NoneType]
            Close the browser process on SIGHUP. Defaults to `true`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds to wait for the browser instance to start. Defaults to `30000` (30 seconds). Pass `0` to
            disable timeout.
        env : Union[Dict[str, Union[bool, float, str]], NoneType]
            Specify environment variables that will be visible to the browser. Defaults to `process.env`.
        headless : Union[bool, NoneType]
            Whether to run browser in headless mode. More details for
            [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode). Defaults to `true` unless the
            `devtools` option is `true`.
        devtools : Union[bool, NoneType]
            **Chromium-only** Whether to auto-open a Developer Tools panel for each tab. If this option is `true`, the `headless`
            option will be set `false`.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings.
        downloads_path : Union[pathlib.Path, str, NoneType]
            If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is
            deleted when browser is closed.
        slow_mo : Union[float, NoneType]
            Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on.
            Defaults to 0.
        viewport : Union[{width: int, height: int}, NoneType]
            Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport.
        no_viewport : Union[bool, NoneType]
            Does not enforce fixed viewport, allows resizing window in the headed mode.
        ignore_https_errors : Union[bool, NoneType]
            Whether to ignore HTTPS errors during navigation. Defaults to `false`.
        java_script_enabled : Union[bool, NoneType]
            Whether or not to enable JavaScript in the context. Defaults to `true`.
        bypass_csp : Union[bool, NoneType]
            Toggles bypassing page's Content-Security-Policy.
        user_agent : Union[str, NoneType]
            Specific user agent to use in this context.
        locale : Union[str, NoneType]
            Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language`
            request header value as well as number and date formatting rules.
        timezone_id : Union[str, NoneType]
            Changes the timezone of the context. See
            [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)
            for a list of supported timezone IDs.
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        permissions : Union[List[str], NoneType]
            A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more
            details.
        extra_http_headers : Union[Dict[str, str], NoneType]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        offline : Union[bool, NoneType]
            Whether to emulate network being offline. Defaults to `false`.
        http_credentials : Union[{username: str, password: str}, NoneType]
            Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).
        device_scale_factor : Union[float, NoneType]
            Specify device scale factor (can be thought of as dpr). Defaults to `1`.
        is_mobile : Union[bool, NoneType]
            Whether the `meta viewport` tag is taken into account and touch events are enabled. Defaults to `false`. Not supported
            in Firefox.
        has_touch : Union[bool, NoneType]
            Specifies if viewport supports touch events. Defaults to false.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. See
            `page.emulate_media()` for more details. Defaults to `'light'`.
        accept_downloads : Union[bool, NoneType]
            Whether to automatically download all the attachments. Defaults to `false` where all the downloads are canceled.
        chromium_sandbox : Union[bool, NoneType]
            Enable Chromium sandboxing. Defaults to `true`.
        record_har_path : Union[pathlib.Path, str, NoneType]
            Path on the filesystem to write the HAR file to.
        record_har_omit_content : Union[bool, NoneType]
            Optional setting to control whether to omit request content from the HAR. Defaults to `false`.
        record_video_dir : Union[pathlib.Path, str, NoneType]
            Path to the directory to put videos into.
        record_video_size : Union[{width: int, height: int}, NoneType]
            Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into
            800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will
            be scaled down if necessary to fit the specified size.

        Returns
        -------
        BrowserContext
        """

        return mapping.from_impl(
            await self._async(
                "browser_type.launch_persistent_context",
                self._impl_obj.launch_persistent_context(
                    userDataDir=user_data_dir,
                    channel=channel,
                    executablePath=executable_path,
                    args=args,
                    ignoreDefaultArgs=ignore_default_args,
                    handleSIGINT=handle_sigint,
                    handleSIGTERM=handle_sigterm,
                    handleSIGHUP=handle_sighup,
                    timeout=timeout,
                    env=mapping.to_impl(env),
                    headless=headless,
                    devtools=devtools,
                    proxy=proxy,
                    downloadsPath=downloads_path,
                    slowMo=slow_mo,
                    viewport=viewport,
                    noViewport=no_viewport,
                    ignoreHTTPSErrors=ignore_https_errors,
                    javaScriptEnabled=java_script_enabled,
                    bypassCSP=bypass_csp,
                    userAgent=user_agent,
                    locale=locale,
                    timezoneId=timezone_id,
                    geolocation=geolocation,
                    permissions=permissions,
                    extraHTTPHeaders=mapping.to_impl(extra_http_headers),
                    offline=offline,
                    httpCredentials=http_credentials,
                    deviceScaleFactor=device_scale_factor,
                    isMobile=is_mobile,
                    hasTouch=has_touch,
                    colorScheme=color_scheme,
                    acceptDownloads=accept_downloads,
                    chromiumSandbox=chromium_sandbox,
                    recordHarPath=record_har_path,
                    recordHarOmitContent=record_har_omit_content,
                    recordVideoDir=record_video_dir,
                    recordVideoSize=record_video_size,
                ),
            )
        )


mapping.register(BrowserTypeImpl, BrowserType)


class Playwright(AsyncBase):
    def __init__(self, obj: PlaywrightImpl):
        super().__init__(obj)

    @property
    def devices(self) -> typing.Dict:
        """Playwright.devices

        Returns a dictionary of devices to be used with `browser.new_context()` or `browser.new_page()`.

        ```py
        import asyncio
        from playwright.async_api import async_playwright

        async def run(playwright):
            webkit = playwright.webkit
            iphone = playwright.devices[\"iPhone 6\"]
            browser = await webkit.launch()
            context = await browser.new_context(**iphone)
            page = await context.new_page()
            await page.goto(\"http://example.com\")
            # other actions...
            await browser.close()

        async def main():
            async with async_playwright() as playwright:
                await run(playwright)
        asyncio.run(main())
        ```

        Returns
        -------
        Dict
        """
        return mapping.from_maybe_impl(self._impl_obj.devices)

    @property
    def selectors(self) -> "Selectors":
        """Playwright.selectors

        Selectors can be used to install custom selector engines. See [Working with selectors](./selectors.md) for more
        information.

        Returns
        -------
        Selectors
        """
        return mapping.from_impl(self._impl_obj.selectors)

    @property
    def chromium(self) -> "BrowserType":
        """Playwright.chromium

        This object can be used to launch or connect to Chromium, returning instances of `ChromiumBrowser`.

        Returns
        -------
        BrowserType
        """
        return mapping.from_impl(self._impl_obj.chromium)

    @property
    def firefox(self) -> "BrowserType":
        """Playwright.firefox

        This object can be used to launch or connect to Firefox, returning instances of `FirefoxBrowser`.

        Returns
        -------
        BrowserType
        """
        return mapping.from_impl(self._impl_obj.firefox)

    @property
    def webkit(self) -> "BrowserType":
        """Playwright.webkit

        This object can be used to launch or connect to WebKit, returning instances of `WebKitBrowser`.

        Returns
        -------
        BrowserType
        """
        return mapping.from_impl(self._impl_obj.webkit)

    def stop(self) -> NoneType:
        """Playwright.stop

        Terminates this instance of Playwright in case it was created bypassing the Python context manager. This is useful in
        REPL applications.

        ```py
        >>> from playwright.sync_api import sync_playwright

        >>> playwright = sync_playwright().start()

        >>> browser = playwright.chromium.launch()
        >>> page = browser.new_page()
        >>> page.goto(\"http://whatsmyuseragent.org/\")
        >>> page.screenshot(path=\"example.png\")
        >>> browser.close()

        >>> playwright.stop()
        ```
        """

        return mapping.from_maybe_impl(self._impl_obj.stop())


mapping.register(PlaywrightImpl, Playwright)
