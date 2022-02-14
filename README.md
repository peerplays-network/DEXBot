# DEXBot

**Download the latest release for Windows, OSX and Linux from [here!](https://gitlab.com/PBSA/tools-libs/DEXBot/-/tree/wip-2)

The Dashboard of the GUI version of DEXBot: ![GUI](https://i.imgur.com/dc2FYum.png)

The CLI version of DEXBot in configuration dialog: ![CLI](https://i.imgur.com/RUSv92q.png)

A Trading Bot provided with two very flexible Market Making strategies. Works on "vanilla" Graphene and all exchanges built upon it. Can be customized with additional strategies written in Python3.


DEXBot can be installed from source or by using the excecutable packages for Windows, OSX, and Linux. Packages include the GUI version, but installation from source provides also the CLI version, which can be used on headless servers and Raspberry Pi's.

The provided strategies can be used to bootstrap new markets, to increase liquidity of an asset, or to try to make profits.
The _Relative Orders_ strategy is the one most think of when speaking of _Market Making_. In most markets it requires tweaking and active monitoring, and is most suitable for sideways markets or _Arbitrage Enabling_ markets (between stable or otherwise equivalent assets). _Staggered Orders_ is a "set and forget" strategy, which thrives in uncertain conditions (before price discovery or otherwise volatile conditions). It requires a long time to realize profits, but is likely to do so if it isn't touched in the mean time. It requires little monitoring and no tweaking. New markets and assets should be bootstrapped with _Staggered Orders_ and later improved with _Relative Orders_.

**Make sure to read strategy documentation from the wiki.** [Here](https://link.medium.com/gXkfewn6XR) is a step-by-step guide to get started

## Does it make profit?
If you properly predict future market conditions, you can manage to make profit. All strategies rely on assumptions. The strategies that rely on less assumptions are less risky, and more risky strategies _can_ make more profit. During long declines the effect is decreased losses - not actual profits. So we can only say that it can make profit, without forgetting that it can also make losses. Good luck.

## Installing and running the software


**Warning**: This is highly experimental code! Use at your OWN risk!

## Running in docker

By default, local data is stored inside docker volumes. To avoid loosing configs and data, it's advised to mount custom
directories inside the container as shown below.

```
mkdir dexbot-data dexbot-config
docker run -it --rm -v `pwd`/dexbot-data:/home/dexbot/.local/share blckchnd/dexbot:latest uptick addkey
docker run -it --rm -v `pwd`/dexbot-config:/home/dexbot/.config/dexbot -v `pwd`/dexbot-data:/home/dexbot/.local/share blckchnd/dexbot:latest dexbot-cli configure
```

To run in unattended mode you need to provide wallet passphrase:

```
docker run -d --name dexbot -e UNLOCK=pass -v `pwd`/dexbot-config:/home/dexbot/.config/dexbot -v `pwd`/dexbot-data:/home/dexbot/.local/share blckchnd/dexbot:latest dexbot-cli run
```

Assuming you have created a Docker secret named "passphrase" in your swarm, you can also get it from there:

```
printf <pass> | docker secret create passphrase -
docker run -d --name dexbot -e UNLOCK=/run/secrets/passphrase -v `pwd`/dexbot-config:/home/dexbot/.config/dexbot -v `pwd`/dexbot-data:/home/dexbot/.local/share blckchnd/dexbot:latest dexbot-cli run
```

## Getting help

## Contributing

Install the software, use it and report any problems by creating a ticket.

Before commiting any changes first time, make sure to install pre-commit hooks!

```
pip install -r requirements-dev.txt
pre-commit install
```

# IMPORTANT NOTE

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
