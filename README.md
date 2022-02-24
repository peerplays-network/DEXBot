

## Installing and running the software

**Warning**: This is highly experimental code! Use at your OWN risk!

```
git clone https://gitlab.com/PBSA/tools-libs/DEXBot
cd DEXBot
git checkout devel
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt
cp chains.py env/lib/python3.8/site-packages/bitsharesbase/chains.py
python3 gui.py 
```

For creating worker for test purpose
```
accountname: init0
key: 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
```

# DEXBot

A Trading Bot provided with three very flexible Market Making strategies. Works on Peerplays. Can be customized with additional strategies written in Python3.

DEXBot can be installed from source or by using the excecutable packages for Windows, OSX, and Linux. Packages include the GUI version, but installation from source provides also the CLI version, which can be used on headless servers and Raspberry Pi's.

The provided strategies can be used to bootstrap new markets, to increase liquidity of an asset, or to try to make profits.
The _Relative Orders_ strategy is the one most think of when speaking of _Market Making_. In most markets it requires tweaking and active monitoring, and is most suitable for sideways markets or _Arbitrage Enabling_ markets (between stable or otherwise equivalent assets). _Staggered Orders_ is a "set and forget" strategy, which thrives in uncertain conditions (before price discovery or otherwise volatile conditions). It requires a long time to realize profits, but is likely to do so if it isn't touched in the mean time. It requires little monitoring and no tweaking. New markets and assets should be bootstrapped with _Staggered Orders_ and later improved with _Relative Orders_.

## Does it make profit?
If you properly predict future market conditions, you can manage to make profit. All strategies rely on assumptions. The strategies that rely on less assumptions are less risky, and more risky strategies _can_ make more profit. During long declines the effect is decreased losses - not actual profits. So we can only say that it can make profit, without forgetting that it can also make losses. Good luck.

## Strategies

The strategies are discussed [here](https://gitlab.com/PBSA/tools-libs/DEXBot/-/wikis/Documentation-DEXBot).

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
